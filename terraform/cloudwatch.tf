resource "aws_cloudwatch_log_group" "soc_logs" {
 name              = "/security/logs"
 retention_in_days = 365
}

resource "aws_cloudwatch_metric_alarm" "feed_failure" {
 alarm_name = "CriticalFeedDown"

 metric_name = "FeedHealth"
 namespace   = "Security"

 threshold   = 1
 comparison_operator = "LessThanThreshold"
}
