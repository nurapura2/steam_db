-- refund system
DECLARE
    v_purchase_id INT := 123; --any id which we want to refund
    v_user_id INT;
    v_amount NUMERIC;
BEGIN
    -- loading data 
    SELECT user_id, SUM(price_at_purchase) INTO v_user_id, v_amount 
    FROM purchases_item JOIN purchases USING(purchase_id)
    WHERE purchase_id = v_purchase_id GROUP BY user_id;

    -- trying to delete
    <deleting from library>
    BEGIN
        DELETE FROM library WHERE purchase_id = v_purchase_id;
    EXCEPTION WHEN OTHERS THEN
        RAISE NOTICE 'Game not found in library, skipping deletion.';
    END;

    -- refunding money
    UPDATE wallets SET balance = balance + v_amount WHERE user_id = v_user_id;
    COMMIT;
END;




DECLARE
    r_user RECORD;
    v_game_id INTEGER;
BEGIN
    -- users with more than 20$ spent on completed purchases
    FOR r_user IN
        SELECT p.user_id
        FROM purchases p
        JOIN purchases_item pi ON p.purchase_id = pi.purchase_id
        WHERE p.status = 'completed'
        GROUP BY p.user_id
        HAVING SUM(pi.price_at_purchase) > 20
    LOOP

        -- random game for gift
        SELECT g.game_id
        INTO v_game_id
        FROM games g
        WHERE NOT EXISTS (
            SELECT 1
            FROM library l
            WHERE l.user_id = r_user.user_id
            AND l.game_id = g.game_id
        )
        ORDER BY RANDOM()
        LIMIT 1;

        -- if there is a game to gift, add it to library
        IF v_game_id IS NOT NULL THEN
            INSERT INTO library(user_id, game_id, purchase_id)
            VALUES (r_user.user_id, v_game_id, NULL);
            RAISE NOTICE 'Gifted game % to user %', v_game_id, r_user.user_id;
            r_user.user_id, v_game_id;
        END IF;

    END LOOP;
END;