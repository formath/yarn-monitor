source /opt/mt/hadoop/bin/hadoop_user_login.sh hadoop-mining

echo "============================================================================================================================================================================================"
echo "============================================================================= root.zz01.hadoop-mining.ad-online ============================================================================"
curl -s 'http://zz01-data-hdp-rmha01.mt.com:8088/cluster/scheduler?openQueues=root.zz01#root.zz01.hadoop-mining' | \
grep "root.zz01.hadoop-mining.ad-online" | \
awk 'BEGIN{FS=",";OFS="\t"}{print $1,$3,$4,$7,$9,$12,"root.zz01.hadoop-mining.ad-online"}' | \
python app_monitor.py

echo ""
echo "============================================================================================================================================================================================"
echo "============================================================================= root.zw02.hadoop-mining.ad-online ============================================================================"
curl -s 'http://zw02-data-hdp-rmha01.mt.com:8088/cluster/scheduler?openQueues=root.zw02#root.zw02.hadoop-mining' | \
grep "root.zw02.hadoop-mining.ad-online" | \
awk 'BEGIN{FS=",";OFS="\t"}{print $1,$3,$4,$7,$9,$12,"root.zw02.hadoop-mining.ad-online"}' | \
python app_monitor.py

echo ""
echo "============================================================================================================================================================================================"
echo "========================================================================== root.zw03_training.hadoop-mining.recall ========================================================================="

curl -s 'http://zw03-data-hdp-rm-trainingha01.mt.com:8088/cluster/scheduler?openQueues=root.zw03_training#root.zw03_training.hadoop-mining' | \
grep "root.zw03_training.hadoop-mining.recall" | \
awk 'BEGIN{FS=",";OFS="\t"}{print $1,$3,$4,$7,$9,$12,"root.zw03_training.hadoop-mining.recall"}' | \
python app_monitor.py
