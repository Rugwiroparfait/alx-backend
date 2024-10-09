import kue from 'kue';

// Create an array for blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Create the sendNotification function
function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);  // Track job progress at 0%

  // Check if the phone number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));  // Fail the job
  }

  job.progress(50, 100);  // Track job progress at 50%
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();  // Complete the job
}

// Create a Kue queue
const queue = kue.createQueue();

// Process jobs from the queue `push_notification_code_2` with two jobs at a time
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
