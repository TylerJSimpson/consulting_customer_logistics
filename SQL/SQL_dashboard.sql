--SQL code for dashboard made for a consulting customer
--Dashboard made in Google Data Studio
--'US-' added for heat map drill down

SELECT 
    CarrierName,
    AVG(DATE_DIFF(DeliveryDate, ShipDate, HOUR)) AS AverageShipToDeliver,
    SUM(Buy) AS TotalBuy,
    SUM(Sell) AS TotalSell,
    SUM(Sell-Buy) AS TotalProfitMargin,
    AVG(Sell-Buy) AS AverageProfitMargin,
    SUM(Quotes) AS TotalQuotes,
    ToCity,
    FromCity,
    CONCAT('US-', ToState) AS ToState,
    CONCAT('US-', FromState) AS FromState,
    DeliveryDate,
    COUNT(ShipmentId) AS ShipmentTotal
FROM 
    `REDACTED.REDACTED.REDACTED`
GROUP BY 
    CarrierName,
    ToCity,
    ToState,
    DeliveryDate,
    FromState,
    FromCity
