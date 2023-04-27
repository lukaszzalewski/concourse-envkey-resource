IMAGE_NAME:=justonecommand/concourse-envkey-resource
IMAGE_TAG:=0.0.1

docker_build:
	@pip freeze > requirements.txt
	@docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .

# test_check
# test_check_with_version
# test_in
# test_out