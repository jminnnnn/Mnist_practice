def sigmoid(z):             #if z is a vector or numpy array, numpy automatically applies the funciton sigmoid elementwise. so no need to worry
    return 1.0 / (1.0 + np.exp(-z))

class Network(object):
    def __init__(self, sizes):
        self.num_layers=len(sizes)
        self.sizes=sizes
        self.biases=[np.random.randn(y,1) for y  in sizes[1:]]          #y부터 1까지 랜덤한 숫자 1개. y는 sizes의 1번 인덱스부터 끝까지 하나씩  # randn by numpy generates gaussian distribution 0,1
                                                                        #1st layer is assumed as the input layer. therefore bias is not set for the first layer --> y in sizes[1:]
        self.weights=[np.random.randn(y,x) for x,y in zip(sizes[:-1],sizes[1:])] #sizes contains the number of neurons in the respective layers
                                                                                #net.weigths[1] --> weight that connects the second and the third layer. [0] would be the on that connects the first and the second layer. 

    def feedforward(self,a):
        #return the output of the network if 'a' is input
        for b,w in zip(self.biases, self.weights):
            a=sigmoid(np.dot(w,a)+b)
        return a


    def SGD(self,training_data,epochs,mini_batch_size, eta, test_data=None):
        # train the dnerual network using mini batch stochastic gradient descent. the trainign data is a list of tuples (x,y) representing the training inputs and the desired outputs.
        # the other non-optional parameters are self explanatory. if test_data is provided then the network will be evaluedted against the test data afeer each epoch!, and partial progress printed out
        # this is useful for tracking progress, but slows down subtantially

        if test_data: n_test=len(test_data)
        n=len(training_data)
        for j in range(epochs):
            random.shuffle(training_data)
        mini_batches=[training_data[k:k+mini_batch_size] for k in range(0,n,mini_batch_size)]
        for mini_batch in mini_batches:
            self.update_mini_batch(min_batch,eta)
        if test_data:
            print ("Epoch{0}: {1} / {2}".format(j, self.evaluate(test_data),n_test))
        else:
            print ("Epoch {0} complete".format(j))

    def update_mini_batch(self, mini_batch):
        #'update the network's weights and biasees by applying gradient descent using backpropagartion to a single mii batch. --> the mini-batch is a list of tuples (x,y) and 'eta' is the learning rate
        nabla_b=[np.zeros(b.shape) for b in self.biases]

