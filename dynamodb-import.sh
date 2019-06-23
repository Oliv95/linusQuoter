#!/bin/bash


for file in "$@"
do
	aws dynamodb batch-write-item --request-item file://$file
done

