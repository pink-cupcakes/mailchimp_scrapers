
#Bash file will:
#Each Day:
#1 Look in eventbrite for new purchasers
	#Python 
#2 Place each of those purchaser's data into a data.json file:
	#Python 
#3 Mailchimp will then open that file
	#Bash
#4 For each  contanct it will try to add the person to a mailing list (as a new user)
	#Bash or python
#5 If they exist and it fails, they will update that persons account to reflect the newest information in their account
	#Bash



#1 Finds new eventbrite subscribers and puts them in a json file
#python3 even.py

# Get the Json data into variables in the bash form
# *** Requires you to install jq      sudo apt-get install jq
#value=($(jq -r '.0' subscribers.json))

#echo "${value[@]}"

#declare -A myarray
#declare -A subscriber
#while IFS="=" read -r key value
#do
#    myarray[$key]="$value"
#done < <(jq -r "to_entries|map(\"\(.key)=\(.value)\")|.[]" subscribers.json)
#while IFS="=" read -r key value
#do
# subscriber[$key]="$value"
#done < <(jq -r "to_entries|map(\"\(.key)=\(.value)\")|.[]" myarray[$key])



#echo "${myarray[1]}"

#for key in "${!myarray[@]}"
#do
#    echo "$key = ${myarray[$key]}"
#done

cat subscribers.json | jq '.'

cat subscribers.json | jq '.["2"]["merge_fields"]["FNAME"]'

#hello=""

#hello=($(subscribers.json | jq '.["3"]["merge_fields"]["FNAME"]'))
#cat $hello

FNAME=($(jq -r '.["3"]["merge_fields"]["FNAME"]' subscribers.json))
LNAME=($(jq -r '.["3"]["merge_fields"]["LNAME"]' subscribers.json))
ENDDATE=($(jq -r '.["3"]["merge_fields"]["END1"]' subscribers.json))
CITY=($(jq -r '.["3"]["merge_fields"]["CLASS1CITY"]' subscribers.json))
CLASS=($(jq -r '.["3"]["merge_fields"]["CLASS1"]' subscribers.json))

echo $FNAME $LNAME $ENDDATE $CLASS $CITY

#NEXT CREATE A NEW USER IN MAILCHIMP WITH THE BASH CODE FROM THE WEBSITE



# Write that new user into the system
#curl --request POST \
#--url 'https://us12.api.mailchimp.com/3.0/lists/4a60ee669f/members/' \
#--user 'anystring:4a55a624d3aec306a7af411134eced91-us12' \
#--header 'content-type: application/json' \
#--data '{"email_address":"gates.c.rosse@gmail.com", "merge_fields":{"FNAME":"JIM"}}' \
#--include

#curl --request POST \
#--url 'https://us12.api.mailchimp.com/3.0/lists/4a60ee669f/members/' \
#--user 'anystring:4a55a624d3aec306a7af411134eced91-us12' \
#--header 'content-type: application/json' \
#--data '{"email_address":"gates.c.rosse@gmail.com", "merge_fields":{"FNAME":"JIM"}}' \
#--include



# Might just need this already as JSON, so just cycle through and grab 1 person at a time
# Might need to reorder the json into the appropriate mailchimp layout

member='ad2a82f647b25de3135c59acd2806263'
writedata='{"operations":{"method":"PUT","path":"lists/4a60ee669f/members/'
writedata+=$member
writedata+='","body":"{\"email_address\":\"gates.c.rosse@gmail.com\", \"status_if_new\":\"subscribed\"}"}]}'
echo $writedata

#4a60ee669f/members/

#THIS WORKS
#Takes an array of users as an argument and updates all of them
#I can create a string of all the users in a loops then update them all at once: PUT makes it update existing users and add new users

#Data I need: An MD5 hash of each user's email address


# You have to put all these lines next to eachother with nothing inbetween
curl --request POST \
--url 'https://us12.api.mailchimp.com/3.0/batches' \
--user 'anystring:4a55a624d3aec306a7af411134eced91-us12' \
--header 'content-type: application/json' \
--data $writedata \
--include

#THIS LINE WORKS--data '{"operations": [{"method":"PUT","path":"lists/4a60ee669f/members/ad2a82f647b25de3135c59acd2806263","body":"{\"email_address\":\"gates.c.rosse@gmail.com\", \"status_if_new\":\"subscribed\"}"}]}' \
#--include



#--data '{"operations": [{"method":"PUT","path":"lists/4a60ee669f/members/ad2a82f647b25de3135c59acd2806263","body":"{\"email_address\":\"gates.c.rosse@gmail.com\", \"status_if_new\":\"subscribed\", \"merge_fields\":"{\"FNAME\":\"Rosse\"}" }"}]}' \

#--data '{"operations": [{"method":"PUT","path":"lists/4a60ee669f/members/ad2a82f647b25de3135c59acd2806263","body":"{\"email_address\":\"gates.c.rosse@gmail.com\", \"status_if_new\":\"subscribed\"}"}]}' \
