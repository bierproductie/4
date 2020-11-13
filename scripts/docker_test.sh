#!/usr/bin/env sh
echo "Spinning containers up"
docker-compose up -d

echo "Waiting for database to start"
docker-compose exec -T bierproductie_api \
    ./scripts/wait-for-it.sh bierproductie_api_db:5432 --timeout=0 --strict

echo "Executing Tests"
docker-compose exec -T bierproductie_api make TARGET=local test

echo "Saving coverage.xml file"
docker cp \
    "$(docker-compose ps -q bierproductie_api)":/usr/src/app/coverage.xml \
    coverage.xml
sed -i "s#/usr/src/app/src#/builds/bierproductie/bierproductie_api/src#g" coverage.xml
