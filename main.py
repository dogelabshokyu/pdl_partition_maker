import json

partitions = {
    "Model" : device_model,
    "Version" : fw_version,
    "Build_Time" : fw_build_time,
    "partition_info" : {
        "total_partition" : total_part,
        "section" :
        {
            "Name" : "sdi",
            "MBR" : "MBR 0",
            "Id" : "0x0",
            "Flash" : True,
            "Start" : "0x00000000",
            "Size" : "0x00080000",
            "bytes" : "524288",
            "Blocksize" : "0x00080000",
            "Pagesize" : "0x00000800"
        }
    }
}