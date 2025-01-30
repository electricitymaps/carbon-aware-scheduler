variable "region" {
  type = string
}

variable "project_id" {
  type = string
}


provider "google" {
  project     = var.project_id
  region      = var.region
}


resource "google_storage_bucket" "tasks_bucket" {
  name          = "carbon-aware-tasks"
  location      = var.region
  storage_class = "STANDARD"

  public_access_prevention = "enforced"
}

resource "google_pubsub_topic" "carbon_aware_tasks_to_schedule" {
  name = "carbon-aware-tasks-to-schedule"

  labels = {
    usage = "carbon-aware-scheduler"
  }

  message_retention_duration = "7200s"
}

resource "google_pubsub_subscription" "carbon_aware_tasks_to_schedule_subscription" {
  name  = "carbon-aware-tasks-to-schedule-subscription"
  topic = google_pubsub_topic.carbon_aware_tasks_to_schedule.id
  labels = {
    usage = "carbon-aware-scheduler"
  }

  # 20 minutes
  message_retention_duration = "7200s"
  retain_acked_messages      = false

  ack_deadline_seconds = 60

  expiration_policy {
    ttl = ""
  }
  retry_policy {
    minimum_backoff = "10s"
  }

  enable_message_ordering    = true
}