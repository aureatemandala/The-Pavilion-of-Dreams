#!/bin/bash

function start_service(){
    uwsgi --ini /DATAFILES/The-Pavilion-of-Dreams/website/uwsgi_conf/uwsgi.ini
    printf "已启动uwsgi\n"
}

function stop_service(){
    uwsgi --stop /DATAFILES/The-Pavilion-of-Dreams/website/uwsgi_conf/uwsgi.pid
    printf "已停止uwsgi\n"
}


case $1 in
    start)
        start_service
        ;;
    stop)
        stop_service
        ;;
    *)
        printf "请输入以下参数以执行命令 {stop|start}"
esac