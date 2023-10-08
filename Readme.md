# Kubernetes

I like learning new technologies. I like doing it by trying to understand the high level picture first, but I also like getting my hands dirty. When doing so, I like to keep the code with the lowest possible complexity needed to be able to put in practice the concepts that I am learning. This is an attempt to do that for Kubernetes.


## Introduction

This is a small project in which I am teaching myself about the Kubernetes API's while building minimal examples that use the concepts that I have learned. The idea is to set incremental goals based on some key concepts, such as 

1. Pods,
2. Services,
3. Ingresses,
4. Deployments,
5. Etc

This is work in progress so more items will show up. 


## The cluster

Given that this exercise is focused on the Kubernetes API's (mostly on `kubectl` and the resources API's), the choice of the cluster implementation is not very relevant. In my personal case I used [k3s](https://k3s.io/) as the distribution, as it is a lightweight and easy to install distribution that doesn't take up too much resources to run. For the container runtime I used [docker](https://www.docker.com/), as it is something that I already use on my daily life.


## The goals

Here I will describe some of the milestones that I want to reach as part of this learning process. This list is not complete and it will keep evolving as I move forward. Most of these goals 

- [x] Create a **pod** for an app that can use `curl` (app/caller).
- [x] Create a **deployment** for an app that has a simple endpoint that can listen to a `GET` call (app/api).
- [x] Update the caller app from a pod manifest to a deployment.
- [x] Add a health check to the api.
- [x] Create a **service** for the app endpoint, and call it from the pod that can use `curl`.
- [x] Create a **service account** that allows to access the kubernetes dashboard.
- [x] Create an **ingress** that allows accessing the endpoint from outside the cluster.
- [X] Create a cronjob that periodically reaches the api from the caller.
- [ ] Add a secret for handling the authentication to the api.
- [ ] Add a volume to store logs.
- [ ] Set up a **load balancer** for the api.
- [ ] Set up a **horizontal pod autoscaler** for the api.
- [ ] Stress test the api and see how the cluster responds.
- [ ] Add Helm.
- etc


## Some extra comments

Some extra comments regarding some of the points above:

1. For the ingress controller I have obscured the domain that I use to expose the service for privacy reasons.
2. For the api implementation I have used the absolute minimum code that I could in order to have a working service. Don't expect anything fancy.
3. To make the ingress work directing the trafic from the domain to the machine running the cluster, a forwarding rule had to be put in place at the router level.
