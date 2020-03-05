import requests
# from bs4 import BeautifulSoup

headers= {
'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
'host': 'buy.housefun.com.tw'
}
url='https://buy.housefun.com.tw/?pg=1'

cookietmp ='__gads=ID=d15e049c04d87714:T=1582266607:S=ALNI_MZ9habTZSTzD5G1_AFrOt-Jd9Qv2A; _gcl_au=1.1.2010896750.1582266608; SEID_G=ef7dfd3d-b491-4fe7-bc41-c13b3eb525bd; TRID_G=553a4358-238b-4f95-967f-e5818b4044e2; __ltm_https_flag=true; __ltmwga=utmcsr=google|utmcmd=organic; _fbp=fb.2.1582266613047.1901873960; _ss_pp_id=dc9ae2f7559f14742d71582238524039; userid=68746fac-13cb-4d3f-a125-fb2592bd03d3; RRD=JN0vIEkfeubATJ91ZsI9*J3s1v-rJjcv; TS012304eb=01aebff41478657c010055165241510daee7c963dd72d750c17009e55b761fa2a2c818f92ae2027b5767d41b25b0d82042b07e16b3046f9bac20dc8b762e41e2884709a6d06265f21bd7eeead37c61093ecb5eda584c9c481ff3152bec5875aad68bbb9f88; _td=e1f589e4-dea8-4456-9fad-e2182da5c1d8; ASP.NET_SessionId=jqxmrmet2yo3zplsioum35qe; yawbewkcehc=0; __lt__cid=5d75303d-986d-4a9e-bd0e-46c69df5a739; _ga=GA1.4.2080110557.1583127053; search_buy_searchMode="1"; search_buy_price="-"; search_buy_regArea="-"; search_buy_room="-"; search_buy_buildAge="-"; search_buy_unitPrice="-"; search_buy_caseFloor="-"; search_buy_caseType=""; search_buy_purpose=""; search_buy_tag=[]; search_buy_parkingType=""; _gid=GA1.4.794857574.1583386763; search_buy_district={"county":"%E5%8F%B0%E5%8C%97%E5%B8%82","district":""}; __LastReferenceId=c7e29b289a; TS3ef6112b_76=08c6b07f08ab2800fc8d445790603e5a1969c95fcde3f2646ac62f8351e6f22ee9af2ad6809686e5236e38c07b47a26f08023adb8f09e8002f04e0182b55dd125659e1356b3698655ac6794a81132228e429498ed7c63355d288db4d2aa96639ee487996c5e3fc97109608b5f9383923fab84eaafae71c23682dd04037120bcc6fb1fe0c97c22f692f939a4efb4828c4e493f959919759222e4f023590de498534caf86b6178d51cc4c2efb2c249688f2274f1763f761bc776ec39ef91a3045019c0369f29ae10ed9f8de4fbbf7fcc08f50895156e8c1ec44b5759930ba214c038f7335144db1a398d6df20077bf5faca5f2553cbb31494f1ef2b7a1957013ae76a4ec16b9206f52f6f4ed05e4bfc4eee4c30ee66d05758884c0a3f433cb51a9; TSPD_101=08c6b07f08ab2800fc8d445790603e5a1969c95fcde3f2646ac62f8351e6f22ee9af2ad6809686e5236e38c07b47a26f:08c6b07f08ab2800fc8d445790603e5a1969c95fcde3f2646ac62f8351e6f22ee9af2ad6809686e5236e38c07b47a26f08023adb8f063800fd7fa082bb15933b1e1d42fa050a46253b03ca9d806acf4d66ac17216da87b6c55e007a0250a8040510e5c58f0dfc2dfd3f783be5d0eebae; TS01424a4d=01aebff414f829ddd4459c1eb8064369852cbb5a73be6bcc8a359d23b01c7f0bb9c8b737a4da023e9405f2607a52586f0806a581579abbc3d85027ab8842634af5d3e4c1c61221f249b374596fa110625d2500b820; __lt__sid=9d171484-91e7c912; TS01a5ae52=01aebff414a9679985d3907e1344db738e827f30bd4e9d41cb5d22fd8529f5ff4614a57282277f802712da964e94937f6ca27922a2b8315c6fac776e26dcb5c523545fa6f3; _pk_ref.22.6273=%5B%22%22%2C%22%22%2C1583403040%2C%22https%3A%2F%2Fprice.housefun.com.tw%2F%22%5D; _pk_ses.22.6273=*; TS8899885c_27=08c6b07f08ab20004d07c201fd7bcd5f8062b1a9168b1b8d0ecd85a7e065f203897825c3f79e8ce208198d903d1120006cfdf1c442b4521508bd776c202238697b65e4af94681cbe7d9d3fabba78d987; _dc_gtm_UA-22823074-5=1; _dc_gtm_UA-34471860-1=1; _pk_id.22.6273=eecaa292f0fd029c.1583127053.5.1583403224.1583403039.'

cookies = {}
for i in cookietmp.split(';'):
    key = i.split('=')[0]
    value = i.replace(key + '=', '')
    cookies[key] = value

# print(cookies)
response= requests.get(url, headers=headers, cookies=cookies)
print(response.text)

