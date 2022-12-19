SAM Step Functions 模版
=======================

我的 SAM 我做主。

## 使用方法

```bash
# 确认 AWS CLI 工具安装
aws --version
# 确认 Terraform CLI 工具安装
sam --version
# 克隆 SAM Step Functions 模版库
git clone https://github.com/komavideo/sam-stepfunctions
cd sam-stepfunctions
# 编译工程
sam build
# 部署运行应用程序
sam deploy --guided \
    --profile [aws-profile-name] \
    --stack-name my-stepfunctions

# 异步执行状态机(工作流)
aws stepfunctions start-execution \
    --profile [aws-profile-name] \
    --state-machine-arn [step-function-arn]
```
