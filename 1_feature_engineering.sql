SELECT 
    txn_id,
    sender_id,
    amount,
    txn_time,
    COUNT(*) OVER(
        PARTITION BY sender_id 
        ORDER BY txn_time 
        RANGE BETWEEN INTERVAL '10 minutes' PRECEDING AND CURRENT ROW
    ) as txn_count_10m,
    SUM(amount) OVER(
        PARTITION BY sender_id 
        ORDER BY txn_time 
        RANGE BETWEEN INTERVAL '10 minutes' PRECEDING AND CURRENT ROW
    ) as rolling_sum_10m
FROM fintech_transactions;