import redis from 'redis';

// Create Redis client for subscribing
const subscriber = redis.createClient();

subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

subscriber.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Subscribe to the channel 'holberton school channel'
subscriber.subscribe('holberton school channel');

// When receiving a message, log it to the console
subscriber.on('message', (channel, message) => {
  console.log(message);
  // If the message is "KILL_SERVER", unsubscribe and quit
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe('holberton school channel');
    subscriber.quit();
  }
});

