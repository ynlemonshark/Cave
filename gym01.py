import gym
import numpy as np

env = gym.make("MountainCar-v0")
env.reset()

LEARNING_RATE = .3
DISCOUNT = .95
EPISODES = 25000

SHOW_EVERY = 2000
print(env.observation_space.high)
print(env.observation_space.low)
print(env.action_space.n)

DISCRETE_OS_SIZE = [20] * len(env.observation_space.high)
discrete_os_win_size = (env.observation_space.high - env.observation_space.low) / DISCRETE_OS_SIZE

print(discrete_os_win_size)

q_table = np.random.uniform(low = -2, high = 0, size = (DISCRETE_OS_SIZE + [env.action_space.n]))
print(q_table.shape)
print(q_table)

def get_discrete_state(state):
    discrete_state = (state - env.observation_space.low) / discrete_os_win_size
    return tuple(discrete_state.astype(np.int64))

render = True
#
# for episode in range(EPISODES):
#     #print(episode)
#     if episode % SHOW_EVERY == 0:
#         print(episode)
#         render = True
#     else:
#         render = False

discrete_state = get_discrete_state(env.reset())
print(discrete_state)
done = False

while not done:
    action = np.argmax(q_table[discrete_state])
    new_state, reward, done, _ = env.step(action)

    new_discrete_state = get_discrete_state(new_state)
    #print(episode,reward, new_state,discrete_state)
    if render:
        env.render()
    if not done:
        max_future_q = np.max(q_table[new_discrete_state])
        current_q = q_table[discrete_state + (action, )]

        new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
        q_table[discrete_state + (action, )] = new_q
    elif new_state[0] >= env.goal_position:
        #print(f"we made it on episode{episode}")
        q_table[discrete_state + (action, )] = 0

    discrete_state = new_discrete_state

env.close()
