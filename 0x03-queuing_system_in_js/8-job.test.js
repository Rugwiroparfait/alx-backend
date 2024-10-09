import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    queue = kue.createQueue();  // Create a new queue for each test
  });

  afterEach(() => {
    queue.testMode.clear();     // Clear queue jobs after each test
  });

  test('throws an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs({}, queue)).toThrowError(
      'Jobs is not an array'
    );
  });

  test('creates jobs for each item in the jobs array', (done) => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account',
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    queue.testMode.jobs.forEach((job, index) => {
      expect(job.type).toBe('push_notification_code_3');
      expect(job.data).toEqual(jobs[index]);
    });

    done();
  });

  test('logs events for job completion, failure, and progress', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
    ];

    // Mock console.log
    console.log = jest.fn();

    createPushNotificationsJobs(jobs, queue);

    // Simulate job events
    const job = queue.testMode.jobs[0];

    job.emit('complete');
    expect(console.log).toHaveBeenCalledWith(
      `Notification job ${job.id} completed`
    );

    job.emit('failed', new Error('failed'));
    expect(console.log).toHaveBeenCalledWith(
      `Notification job ${job.id} failed: failed`
    );

    job.emit('progress', 50);
    expect(console.log).toHaveBeenCalledWith(
      `Notification job ${job.id} 50% complete`
    );
  });
});

