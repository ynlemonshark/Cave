import gym
import numpy as np

# MountainCar 에 관한 내용은 C:\ProgramData\Anaconda3\envs\atari_test\Lib\site-packages\gym\envs\classic_control\mountain_car.py 참조
env = gym.make("MountainCar-v0")
env.reset()

LEARNING_RATE = .3
DISCOUNT = .95
EPISODES = 5000

SHOW_EVERY = 2000

# Observation:
# Type: Box(2)
# Num Observation    Min    Max
# 0   Car Position   - 1.2  0.6
# 1   Car Velocity   - 0.07 0.07
# Actions:
# Type: Discrete(3)
# Num   Action
# 0     Accelerate to the Left
# 1     Don't accelerate
# 2     Accelerate to the Right

print(env.observation_space.high)  # [0.6  0.07]
print(env.observation_space.low)   # [-1.2  -0.07]
print(env.action_space.n)          # 3

# observation 하는 값들을 20개의 단계로 나눈다는 의미
# 연속적인 값들을 이산화하는 과정에서 20단계로 만듬
# DISCRETE_OS_SIZE = [20, 20]
DISCRETE_OS_SIZE = [20] * len(env.observation_space.high)

# 한 step당 size를 만듦
discrete_os_win_size = (env.observation_space.high - env.observation_space.low) / DISCRETE_OS_SIZE

# q_table 은 어떻게 생성되는가??

# 1 단계의 값?
print(discrete_os_win_size)  # [0.09  0.007]

# size = (20, 20, 3)
# action에 관련해서 table을 만들음, 그런데 2가아니가 왜 -2 일까?
q_table = np.random.uniform(low = -2, high = 0, size = (DISCRETE_OS_SIZE + [env.action_space.n]))

print(q_table.shape)  # [20, 20, 3]
#print(q_table)

# env.reset()초기값??  position 은 -0.4 ~ -0.6의 값에서, velocity 는 0 초기값을 랜덤하게 부여한다 ? ex: [ -0.534, 0 ] :

# 아래의 함수는 소수점으로 구성되어 있는 값들을 정수들로 바꾸는 역할
def get_discrete_state(state):
    discrete_state = (state - env.observation_space.low) / discrete_os_win_size
    #print(tuple(discrete_state.astype(np.int64)))
    return tuple(discrete_state.astype(np.int64))

render = True
#
for episode in range(EPISODES):
    #print(episode)
    if episode % SHOW_EVERY == 0:
        print(episode)
        render = True
    else:
        render = False

    # state는 (position, velocity)
    discrete_state = get_discrete_state(env.reset())
    #print(discrete_state)
    done = False

    while not done:
        # q table에서 discrete_state 번째 있는 array값중 np.argmax를 통해 가장 큰 값의 index를 action에 넣어준다
        action = np.argmax(q_table[discrete_state])
        # env.step을 통해 action을 넣어주고 새로운 값들에 대한 정보를 받는다. 자세한것을 mountain_car.py 참조
        new_state, reward, done, _ = env.step(action)
        new_discrete_state = get_discrete_state(new_state)
        #print(episode,reward, new_state,discrete_state)
        if render:
            env.render()
        if not done:
            max_future_q = np.max(q_table[new_discrete_state])
            current_q = q_table[discrete_state + (action, )]
            # Q table 생성 식 참조
            new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)

            q_table[discrete_state + (action, )] = new_q
        elif new_state[0] >= env.goal_position:
            #print(f"we made it on episode{episode}")
            q_table[discrete_state + (action, )] = 0

        discrete_state = new_discrete_state

env.close()
