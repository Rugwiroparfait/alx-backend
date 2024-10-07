---

# 0x03. Queuing System in JS

## Description
This project implements a Redis-based queuing system using JavaScript, Node.js, Express.js, and Kue. It demonstrates how to set up a queuing system with Redis, manage job creation and processing, track job progress, and handle errors efficiently using Kue.

## Requirements
- OS: Ubuntu 18.04
- Node.js: 12.x
- Redis: 5.0.7 or higher
- JavaScript files must use the `.js` extension
- All files must end with a new line

## Installation
1. **Install Redis**  
   Download, extract, and compile Redis:
   ```bash
   $ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
   $ tar xzf redis-6.0.10.tar.gz
   $ cd redis-6.0.10
   $ make
   ```
   Start Redis in the background:
   ```bash
   $ src/redis-server &
   ```
   Verify the installation:
   ```bash
   $ src/redis-cli ping
   ```

2. **Install Node.js dependencies**  
   Run the following command in the project directory to install required modules:
   ```bash
   $ npm install
   ```

## Project Files
- **package.json**: Specifies the project dependencies.
- **.babelrc**: Configures Babel for ES6 support.
- **dump.rdb**: Redis dump file.

## Usage
### Running Redis client
To connect a Node.js client to the Redis server, use the following script:
```bash
$ npm run dev 0-redis_client.js
```

### Node Redis Client Operations
Basic Redis operations such as setting and getting values, asynchronous Redis operations, and handling Redis hashes are implemented in the following scripts:
- **0-redis_client.js**: Connects to Redis and handles connection errors.
- **1-redis_op.js**: Performs basic Redis operations using callbacks.
- **2-redis_op_async.js**: Utilizes async/await with Redis using `promisify`.
- **4-redis_advanced_op.js**: Stores and retrieves complex Redis hashes.

### Publisher-Subscriber Model
The system demonstrates a publisher-subscriber queuing model using Redis. The subscriber listens for messages, and the publisher sends messages on the specified channel.
- **5-subscriber.js**: Subscribes to a Redis channel and logs messages.
- **5-publisher.js**: Publishes messages to a Redis channel.

### Job Queuing with Kue
The project includes job queuing using Kue for background processing:
- **6-job_creator.js**: Creates jobs with specific data (phone number, message) and adds them to the `push_notification_code` queue.
- **6-job_processor.js**: Processes jobs from the `push_notification_code` queue and logs notifications.

### New Tasks: Tracking Progress and Errors
#### 8. Track progress and errors with Kue: Create the Job Creator
In **7-job_creator.js**, an array of job data is created. Each job is pushed to the `push_notification_code_2` queue, and its progress, completion, or failure is tracked. The console logs job creation, completion, errors, and progress percentage.

```bash
$ npm run dev 7-job_creator.js
```

#### 9. Track progress and errors with Kue: Create the Job Processor
In **7-job_processor.js**, jobs from the `push_notification_code_2` queue are processed. The processor tracks job progress and handles blacklisted phone numbers. If a phone number is blacklisted, the job fails with an error.

```bash
$ npm run dev 7-job_processor.js
```

#### 10. Writing the job creation function
In **8-job.js**, the `createPushNotificationsJobs` function is defined to create jobs in the queue `push_notification_code_3`. The function tracks job creation, completion, failure, and progress. If the argument `jobs` is not an array, it throws an error.

```bash
$ npm run dev 8-job-main.js
```

### Running Job Queues
Start a Redis server and run the following commands to create and process jobs:
1. Terminal 1: Run the job processor:
   ```bash
   $ npm run dev 6-job_processor.js
   ```
2. Terminal 2: Run the job creator:
   ```bash
   $ npm run dev 6-job_creator.js
   ```

## Project Structure
```
.
├── 0-redis_client.js
├── 1-redis_op.js
├── 2-redis_op_async.js
├── 4-redis_advanced_op.js
├── 5-publisher.js
├── 5-subscriber.js
├── 6-job_creator.js
├── 6-job_processor.js
├── 7-job_creator.js
├── 7-job_processor.js
├── 8-job.js
├── 8-job-main.js
├── .babelrc
├── dump.rdb
├── package.json
├── README.md
```

## Author
This project is part of the **ALX Backend curriculum.
