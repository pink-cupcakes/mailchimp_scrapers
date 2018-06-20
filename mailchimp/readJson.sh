

#FNAME=($(jq -r '.["3"]' subscribers.json))


variable= {
    "email_address": "urist.mcvankab@freddiesjokes.com",
    "status": "subscribed",
    "merge_fields": {
        "FNAME": "Urist",
        "LNAME": "McVankab"
    }
}


#curl --request POST \
#--url 'https://us12.api.mailchimp.com/3.0/batches' \
#--user 'anystring:4a55a624d3aec306a7af411134eced91-us12' \
#--header 'content-type: application/json' \
#--data $writedata \
#--include
