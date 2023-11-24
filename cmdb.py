data = [
        {
            "id" : 1,
            "deviceName" : "Network#1",
            "type" : "Network",
            "deviceType" : "Switch",
            "model" : "N9K-C93180YC-FX3",
            "vendor" : "CISCO",
            "osType" : "NXOS",
            "osVersion" : "10.3(3)N1(1)",
            "ipAddress" : "1.2.3.4",
            "macAddress" : "001d.d89c.f16d",
            "personInChargeId" : "sj1234.park",
            "personInChargeName" : "박프로",
            "subPersonInChargeId" : "sj5321.kim",
            "subPersonInChargeName" : "김프로",
            "OperationStatus" : "Active",
            "installedLocation" : "SUWON DC SUWON-6F-082123",
            "department" : "운영N/W그룹",
            "domain" : "전사 개발망",             
            "Service" : "",           
            "Customer" : "Samsung SDI",
            "connectedDevice": ["Server#1","Network#3"]
        },        
        {
            "id" : 2,
            "deviceName" : "Network#2",
            "type" : "Network",
            "deviceType" : "Router",
            "model" : "N9K-C3300YC-FX3",
            "vendor" : "CISCO",
            "osType" : "NXOS",
            "osVersion" : "10.1(3)N1(1)",
            "ipAddress" : "1.2.3.5",
            "macAddress" : "001d.cd9c.fd6d",
            "personInChargeId" : "sj1234.park",
            "personInChargeName" : "박프로",
            "subPersonInChargeId" : "sj5321.kim",
            "subPersonInChargeName" : "김프로",
            "OperationStatus" : "Active",
            "installedLocation" : "SUWON DC SUWON-6F-082124",
            "department" : "운영N/W그룹",
            "domain" : "전사 개발망",     
            "Service" : "",           
            "Customer" : "Samsung SDI",
            "connectedDevice": ["Network#3","Server#2"]
        },
        {
            "id" : 3,
            "deviceName": "Network#3",
            "type": "Network",
            "deviceType": "Router",
            "model": "N9K-C93180YC-FX3",
            "vendor": "CISCO",
            "osType": "NXOS",
            "osVersion": "10.0(3)N1(1)",
            "ipAddress": "1.2.4.12",
            "macAddress": "001d.cddc.f56d",
            "personInChargeId": "sj1234.park",
            "personInChargeName": "박프로",
            "subPersonInChargeId": "sj5321.kim",
            "subPersonInChargeName": "김프로",
            "OperationStatus": "Active",
            "installedLocation": "SUWON DC SUWON-5F-032124",
            "department": "운영N/W그룹",
            "domain": "전사 개발망",
            "Service": "",
            "Customer": "Samsung SDI",
            "connectedDevice": ["Network#1","Network#2"]
        },
        {
            "id" : 4,
            "deviceName": "Server#1",
            "type": "Server",
            "deviceType": "Linux",
            "model": "ProLiant DL380",
            "osType": "Ubuntu",
            "osVersion": "23.04",
            "vendor": "HPE",
            "ipAddress": "1.2.10.12",
            "macAddress": "001d.cv4c.fddd",
            "personInChargeId": "sj1234.yang",
            "personInChargeName": "양프로",
            "subPersonInChargeId": "sj5321.lee",
            "subPersonInChargeName": "이프로",
            "OperationStatus": "Active",
            "installedLocation": "SUWON DC SUWON-3F-032124",
            "department": "운영서버그룹",
            "domain": "전사 개발망",
            "Service": "ERP 개발서버",
            "Customer": "Samsung SDI",
            "connectedDevice": ["Network#1", "Wildfly#1"]
        },
        {
            "id" : 5,
            "deviceName": "Server#2",
            "type": "Server",
            "deviceType": "Linux",
            "model": "ProLiant DL380",
            "osType": "Ubuntu",
            "osVersion": "23.01",
            "vendor": "HPE",
            "ipAddress": "1.2.10.57",
            "macAddress": "001d.cv4c.f1dd",
            "personInChargeId": "sj1234.yang",
            "personInChargeName": "양프로",
            "subPersonInChargeId": "sj5321.lee",
            "subPersonInChargeName": "이프로",
            "OperationStatus": "Active",
            "installedLocation": "SUWON DC SUWON-3F-032124",
            "department": "운영서버그룹",
            "domain": "전사 개발망",
            "Service": "ERP 개발 DB",
            "Customer": "Samsung SDI",
            "connectedDevice": ["Network#2"]
        },
        {
            "id" : 6,
            "deviceName": "Wildfly#1",
            "type": "Application",
            "deviceType": "",
            "model": "",
            "osType": "Wildfly",
            "osVersion": "28.0.1",
            "vendor": "Redhat",
            "ipAddress": "",
            "macAddress": "",
            "personInChargeId": "sj5321.kim",
            "personInChargeName": "김프로",
            "subPersonInChargeId": "abcd.howang",
            "subPersonInChargeName": "황프로",
            "OperationStatus": "Active",
            "installedLocation": "",
            "department": "운영서버그룹",
            "domain": "전사 개발망",
            "Service": "ERP 개발 DB",
            "Customer": "Samsung SDI",
            "connectedDevice": ["Server#1"]
        }
]