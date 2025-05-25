# Chapter 2: Back of the Envelope Estimation

Estimations that can be done quickly to get a good feel for designs that meet our requirements
 
- Understand the power of two
- latency numbers
- availability numbers

## Power of Two

An ASCII character uses one byte of memory (8 bits)

- Power 10: Thousand 1KB
- Power 20: Million 1MB
- Power 30: Billion 1GB
- Power 40: Trillion 1TB
- Power 50: Quadrillion 1PB


## Latency Numbers

- L1 Cache: 0.5ns
- L2 Cache: 7ns
- Main Memory Reference: 100ns
- 2KB over 1Gpbs network = (1000ns = 1us) 20us
- 1MB from memory = 250us
- Disk Seek = (1,000us = 1ms) 10ms
- 1MB from disk = 30ms
- Packet CA -> NED -> CA = 150ms

## Availability Numbers

- 99% is 3.65 days per year
- 99.99% is 8 hours per year
- 99.99% is 1 hour per year
- 99.999% is 5 minutes year
- 99.9999% is 30 seconds per year

Estimate QPS(query per second) of twitter

Usage
- 300 miliion users
- 50% users per day
- 10% contain media
- 5 Years
- 2 tweets per day

Tweet 
- id 64bytes
- text 140bytes
- media 1mb or 1million bytes


Estimation QPS
1. 150 million users per day doing 2 tweets
2. 300 million tweets per day or ~4000 Tweets Per Second
3. Peek QPS: 2*QPS = ~8000

Data Costs
1. 10% tweets are 1MB 90% of the tweets are 200bytes (neglible)
2. .10 * 1MB * 300,000,000 tweets per day * 365 * 5
3. 550000000000MB or 55PB


