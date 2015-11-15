#!/usr/bin/python
#coding:utf-8
from spidertool import SQLTool ,config
from ..model import ipmain


limitpage=15
DBhelp=SQLTool.DBmanager()
localconfig=config.Config()
def ipshow(ip='',vendor='',osfamily='',osgen='',accurate='',updatetime='',hostname='',state='',page='0'):
    validresult=False
    request_params=[]
    values_params=[]
    if ip!='':
        request_params.append('ip')
        values_params.append(SQLTool.formatstring(ip))
    if vendor!='':
        request_params.append('vendor')
        values_params.append(SQLTool.formatstring(vendor))
    if osfamily!='':
        request_params.append('osfamily')
        values_params.append(SQLTool.formatstring(osfamily))
    if osgen!='':
        request_params.append('osgen')
        values_params.append(SQLTool.formatstring(osgen))
    if accurate!='':
        request_params.append('accurate')
        values_params.append(SQLTool.formatstring(accurate))
    if updatetime!='':
        request_params.append('updatetime')
        values_params.append(SQLTool.formatstring(updatetime))
    if hostname!='':
        request_params.append('hostname')
        values_params.append(SQLTool.formatstring(hostname))
    if state!='':
        request_params.append('state')
        values_params.append(SQLTool.formatstring(state))
    DBhelp.connectdb()
    table=localconfig.iptable
    result,content,count,col=DBhelp.searchtableinfo_byparams([table], ['ip','vendor','osfamily','osgen','accurate','updatetime','hostname','state'], request_params, values_params)

    if count == 0:
        pagecount = 0;
    elif count %limitpage> 0:
#         pagecount = math.ceil(count / limitpage)
        pagecount=int((count+limitpage-1)/limitpage) 


    else:
        pagecount = count / limitpage

    print pagecount
    if pagecount>0:
    
        limit='    limit  '+str(page)+','+str(limitpage)
        result,content,count,col=DBhelp.searchtableinfo_byparams([table], ['ip','vendor','osfamily','osgen','accurate','updatetime','hostname','state'], request_params, values_params,limit,order='updatetime desc')
    
        DBhelp.closedb()
        ips=[]
        if count>0:
            validresult=True
            for temp in result :
                aip=ipmain.Ip(ip=temp[0],vendor=temp[1],osfamily=temp[2],osgen=temp[3],accurate=temp[4],updatetime=temp[5],hostname=temp[6],state=temp[7])
                ips.append(aip)
        return ips,count,pagecount
    return [],0,pagecount
##count为返回结果行数，col为返回结果列数,count,pagecount都为int型

def ipadd(ip):
    nowip=ip.getIP()
    vendor=ip.getVendor()
    osfamily=ip.getOsfamily()
    state=ip.getState()
    osgen=ip.getOsgen()
    updatetime=ip.getUpdatetime()
    accurate=ip.getAccurate()
    hostname=ip.getHostname()

    
    
    
    request_params=[]
    values_params=[]
    if nowip!='':
        request_params.append('ip')
        values_params.append(nowip)
    if vendor!='':
        request_params.append('vendor')
        values_params.append(vendor)
    if osfamily!='':
        request_params.append('osfamily')
        values_params.append(osfamily)
    if state!='':
        request_params.append('state')
        values_params.append(state)
    if osgen!='':
        request_params.append('osgen')
        values_params.append(osgen)
    if updatetime!='':
        request_params.append('updatetime')
        values_params.append(updatetime)
    if accurate!='':
        request_params.append('accurate')
        values_params.append(accurate)
    if hostname!='':
        request_params.append('hostname')
        values_params.append(hostname)
   
    table=localconfig.iptable
    DBhelp.connectdb()

    tempresult=DBhelp.replaceinserttableinfo_byparams(table, request_params, [tuple(values_params)])
    DBhelp.closedb()

    return tempresult

    
    