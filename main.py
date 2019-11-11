import json
device_model = "IM-A910S"
fw_version = "S0225122"
fw_build_time = "Jan 13 201517:23:48"
'''
partitions = {
    "PDL_Partition": {
        "Model" : device_model,
        "Version" : fw_version,
        "Build_Time" : fw_build_time,
        "partition_info" : {
            "section" : {
                "no1" : 10,
                "no2" : 0,
                "flash" : "Yes",
                "start" : 0,
                "zero" : 0,
                "size1" : 524288,
                "size2" : 524288,
                "blocksize" : 524288,
                "pagesize" : 2048,
                "none" : "b'\xff\xff\xff\xff\xff\xff\xff\xff\xf0\xff\xff\xff\xff\xff\xff\xff'",
                "name" : "phoneinfo",
                "no" : 10,
                "type" : "MBR"
            }
        }
    }
}
'''

#partitions = {}
'''
section_num = 13
for i in range(section_num):
    num = "section"+str(i)
    print(num)
'''
section_num = 13
partitions = {"PDL_Partitions" : {}}
partitions["PDL_Partitions"] = {"Model" : device_model, "Version" : fw_version, "Build_time" : fw_build_time, "Partition_info" : {}}
for i in range(section_num):
    sector_name = "section" + str(i)
    sector_dict = {sector_name: {"no1" : 10,
                                 "no2" : 0,
                                 "flash" : "Yes",
                                 "start" : 0,
                                 "zero" : 0,
                                 "size1" : 524288,
                                 "size2" : 524288,
                                 "blocksize" : 524288,
                                 "pagesize" : 2048,
                                 "none" : "b'\xff\xff\xff\xff\xff\xff\xff\xff\xf0\xff\xff\xff\xff\xff\xff\xff'",
                                 "name" : "phoneinfo",
                                 "no" : 10,
                                 "type" : "MBR"}}
    partitions["PDL_Partitions"]["Partition_info"].update(sector_dict)


print(json.dumps(partitions, ensure_ascii=False, indent="\t"))