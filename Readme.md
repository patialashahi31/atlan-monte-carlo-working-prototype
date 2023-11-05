# (INBOUND, EXTERNAL) : A customer uses Monte Carlo as a tool for data observability. They have set it up so that Monte Carlo catches any table health or data reliability issues early on. The customer would like Atlan to also become a near-real-time repository of such issues, with relevant metadata attached to respective assets.

### monte_carlo_producer.py will be generating random alerts and kafka consumer will consume it and save in Cassandra as well

## Local Setup

```bash
make up

```
<img width="1123" alt="Screenshot 2023-11-05 at 12 05 42 AM" src="https://github.com/patialashahi31/atlan-monte-carlo-working-prototype/assets/40652331/3b77f30f-2cac-43a1-bf28-9a6b8d5969e8">
