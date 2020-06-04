#!/bin/bash

TABLES="client_eod_statistic client_eod_position model_parameters \
        model_configuration private_message_index execution_report \
        new_order_single order_cancel_replace_request order_cancel_request \
        private_fix_message order_request_trigger_event_index"
# order_request_trigger_event_index

mysqldump -uroot -proot1234 -h127.0.0.1 -P3306 epsilon $TABLES > .t.sql
gzip .t.sql
