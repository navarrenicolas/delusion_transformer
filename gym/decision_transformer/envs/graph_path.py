import gym
from gym import spaces

class GraphShortestPathEnv(gym.Env):
    def __init__(self, graph, start_node, end_node):
        super(GraphShortestPathEnv, self).__init__()
        self.graph = graph
        self.start_node = start_node
        self.end_node = end_node
        self.current_node = start_node
        
        self.action_space = spaces.Discrete(len(graph))
        self.observation_space = spaces.Discrete(len(graph))
        
    def reset(self):
        self.current_node = self.start_node
        return self.current_node
    
    def step(self, action):
        if action in self.graph[self.current_node]:
            self.current_node = action
        
        done = self.current_node == self.end_node
        reward = -self.graph[self.current_node][action].get('weight', 1)
        
        return self.current_node, reward, done, {}
    
    def render(self, mode='human'):
        pass
    
    def close(self):
        pass

# Initialize the environment
env = GraphShortestPathEnv(G, start_node=1, end_node=4)

