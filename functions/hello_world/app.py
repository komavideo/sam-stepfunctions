import random

def lambda_handler(event, context):
    todoList = ["游泳", "爬山", "吃冰淇淋"]
    return {
        'statusCode': 200,
        'body': random.choice(todoList),
    }
