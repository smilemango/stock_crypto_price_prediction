#!/bin/sh

hyperopt-mongo-worker --mongo=localhost:27017/hyperopt_db --poll-interval=0.1
