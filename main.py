def apply_weight_decay(parameters: list[list[float]], gradients: list[list[float]], 
                       lr: float, weight_decay: float, apply_to_all: list[bool]) -> list[list[float]]:
    result = []
    for params, grads in zip(parameters, gradients):
        for param, grad in zip(params, grads):
            new_param = param - lr * (grad + weight_decay * param)
            result.append(new_param)
    return result

parameters=[[1.0, 2.0]]
gradients=[[0.1, 0.2]]
lr=0.1
weight_decay=0.01
apply_to_all=[True]
print(
    apply_weight_decay(parameters, gradients, lr, weight_decay, apply_to_all)
)