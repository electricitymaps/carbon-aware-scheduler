# carbon-aware-scheduler
A cloud carbon aware scheduler using the carbon aware sdk

## Initial infrastructure setup

First export the following environment variables:
```
export TF_VAR_region=<your gcp region>
export TF_VAR_project_id=<your gcp project id>
```
Then run the following commands:
```bash
terraform init
terraform plan
terraform apply
```

## Running the scheduler

First export the following environment variables:
```bash
export CARBON_AWARE_TASK_BUCKET=<your gcp bucket>
export CARBON_AWARE_PUBSUB_SUBSCRIPTION=<your gcp pubsub subscription>
```