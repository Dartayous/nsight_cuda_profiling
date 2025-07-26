## 🧠 Summary of the Change
This update introduces a structured PR template that:

- 📌 Prompts contributors to clearly summarize their changes

- 🔗 Encourages linking related issues or feature requests

- 🧪 Promotes consistent testing and review practices

- ✅ Ensures commits follow your coding standards and documentation guidelines


## 🚧 What Problem It Solves
### Before this, contributors (including future-you!) could create pull requests with little or no context. That leads to:

- Time wasted deciphering change intent

- Inconsistent documentation or review criteria

- Missed bugs or skipped testing steps

Now you’ve got a contributor checklist built right into GitHub’s UI, streamlining review, improving collaboration, and preserving clarity across development cycles. 🎯

## 📂 Related Issue

## Issue #1 – CUDA Kernel Optimization Logging
### 🚀 CUDA Kernel Optimization Logging

We conducted detailed profiling on custom CUDA kernels using Nsight Compute. This issue tracks the addition of documentation (`warp_efficiency.md`) capturing warp execution patterns, memory throughput, and kernel behavior analysis.

**Labels:** enhancement, documentation  


## Issue #2 – PR Template Setup
### 📑 Add PR Template for Contributor Consistency

Standardized pull request reviews by adding `.github/pull_request_template.md`. This ensures future contributions follow a checklist for testing, documentation, and code clarity.

**Labels:** documentation, workflow  


## Issue #3 – Branching & Development Workflow
### 🌱 Initialize Branching and Development Flow

Created and pushed code to the `dev` branch, establishing a clean development pipeline. This isolates feature work and enables structured pull request reviews via GitHub’s compare functionality.

**Labels:** workflow  


## Issue #4 – Triton Deployment Preparation
### 🧩 Prepare Repo for Triton Model Deployment

Set up project structure and documentation for deploying AI models using Nvidia Triton Inference Server. This includes laying groundwork for config files, deployment automation, and benchmarking scripts.

**Labels:** infrastructure, enhancement  


## Issue #5 – FastAPI Routing Debug
### 🐞 Debug and Validate FastAPI Endpoints

Fixed route-handling logic and confirmed model inference works through FastAPI. This issue marks our testing and validation efforts that confirmed endpoint reliability.

**Labels:** bug, testing  



## 🔍 Key Changes

- [ ] Describe major updates or new features
- [ ] Highlight structural or logic changes
- [ ] Note any new dependencies or scripts

## ✅ Checklist

- [ ] I tested the code locally
- [ ] I’ve added relevant comments and documentation
- [ ] I’ve assigned reviewers or labeled the PR appropriately
- [ ] This PR follows the coding style and contribution guide

## 💬 Notes

<!-- Anything special reviewers should keep in mind. -->

