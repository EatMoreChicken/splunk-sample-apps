# Splunk TA Astro
This TA is a simple example of conducting an API integration for Splunk. The example uses a public API to pull information regarding the International Space Station and people in space. The goal of the app to for users to craft their own app using the requirements below and compare the requirements with this app.

## To-Do
- [ ] Add versioning information into `app.conf`
- [ ] Add Add-On GUI with Inputs and Configuration pages
- [ ] Populate sourcetype parameters within `props.conf`

## Requirements
Using Python packaged with Splunk, create an app to ingest logs about people currently in space and location information of the ISS using the publicly accessible APIs provided below.

Additional Requirements:
- The logs must be ingested in `JSON` format to prevent the need to create field extractions within Splunk.
- Logs can be placed in any index.
- ISS location information should be placed into a sourcetype named `astro:iss` and data should be queried every 2 minutes.
- Information about people in space should be placed in a sourcetype named `astro:people` and data should be queried every 5 minutes.
