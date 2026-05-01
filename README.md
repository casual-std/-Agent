# CodeGuard - 智能代码评审 Agent

该项目是一个基于 Python 和 Pylint 的智能代码评审工具。通过集成到 GitHub 的 CI/CD 流程中，它能够在每次 PR 提交时自动进行代码审查，并生成评审反馈。

## 项目功能
1. 运行 Pylint 执行代码风格检查。
2. 基于预训练的机器学习模型生成代码评审反馈。
3. 自动生成并保存评审报告。

## 项目结构
- `agent/code_review_agent.py`: 代码评审代理类实现
- `ci/.github/workflows/code_review.yml`: GitHub Actions CI 配置
- `sample_code/`: 示例代码目录，用于测试评审代理

## 安装依赖
```bash
pip install -r requirements.txt
```

## 使用
1. 在 GitHub 上创建一个仓库，并将代码推送到仓库。
2. 配置 `.github/workflows/code_review.yml`，将代码评审代理集成到 CI 流程中。
3. 创建一个 Pull Request，Agent 将自动运行并生成评审报告。

## 注意事项
请确保已经训练并保存了一个机器学习模型（`review_model.pkl`）。可以根据实际需要修改评审模型和参数。
