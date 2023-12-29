SELECT 
    t.name AS TableName,
    ds.name AS DataSpaceName,
    p.partition_number,
    fg.name AS FileGroupName,
    df.name AS FileName,
    df.physical_name AS PhysicalFileName
FROM 
    sys.tables t
JOIN 
    sys.indexes i ON t.object_id = i.object_id
JOIN 
    sys.partitions p ON i.object_id = p.object_id AND i.index_id = p.index_id
JOIN 
    sys.destination_data_spaces dds ON p.partition_number = dds.destination_id
JOIN 
    sys.data_spaces ds ON dds.data_space_id = ds.data_space_id
JOIN 
    sys.filegroups fg ON ds.data_space_id = fg.data_space_id
JOIN 
    sys.database_files df ON fg.data_space_id = df.data_space_id
WHERE 
    t.name = 'TwojaNazwaTabeli' -- Zastąp 'TwojaNazwaTabeli' rzeczywistą nazwą tabeli
ORDER BY 
    p.partition_number;
