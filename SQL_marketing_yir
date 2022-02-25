--SQL code for a customer for a year-in-review for their top customers
--Year in review PDF created in Google Data Studio
--zip codes joined to create an interactive lane analysis via flowmap.blue

SELECT 
    Customer,
    Shipment_ID,
    Shipper_Name,
    Pickup_Date,
    Estimated_Delivery_Date,
    AVG(DATE_DIFF(Estimated_Delivery_Date, Pickup_Date, DAY)) AS Estimated_Delivery_Time,
    Shipper_City,
    Shipper_Zip,
    CONCAT('US-', Shipper_State) AS Ship_State,
    Consignee_City,
    Consignee_Zip,
    CONCAT('US-', Consignee_State) AS Deliver_State,
    CONCAT(Shipper_City, "-", Consignee_City) AS Lane,
    AVG(Mileage) AS Avg_Mileage,
    Mileage,
    AVG(Weight) AS Avg_Weight,
    Weight,
    Commodity_Description,
    zip.LAT AS Shipper_Lat,
    zip.LNG AS Shipper_Lng,
    zip2.LAT AS Consignee_Lat,
    zip2.LNG AS Consignee_Lng
FROM 
    `REDACTED.REDACTED.REDACTED` cust
    JOIN
        `REDACTED.REDACTED.zip_code` zip
    ON 
        cust.Shipper_Zip = zip.ZIP
    JOIN
        `REDACTED.REDACTED.REDACTED` zip2
    ON 
        cust.Consignee_Zip = zip2.ZIP
GROUP BY 
    Customer,
    Shipment_ID,
    Pickup_Date,
    Shipper_Name,
    Shipper_City,
    Ship_State,
    Consignee_City,
    Deliver_State,
    Mileage,
    Weight,
    Estimated_Delivery_Date,
    Commodity_Description,
    Shipper_Zip,
    Consignee_Zip,
    zip.LAT,
    zip.LNG,
    zip2.LAT,
    zip2.LNG
