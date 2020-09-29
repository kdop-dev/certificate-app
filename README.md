# Certificate-app

Print a custom pdf (certificate).

Developed for a workshop to demostrate docker command and kubernetes deployment with ingress.

## Requirements

* Docker or Docker Desktop
* Kubernetes cluster or Kuberntes from docker Desktop enabled
* Ingres controller installed on cluster or [install ingress controller](https://kubernetes.github.io/ingress-nginx/deploy/#docker-for-mac) on kubernets (remote cluster or desktop)

> It was tested on Docker Desktop for Mac and AKS.

## Install on k8s cluster

```bash
helm upgrade --install --namespace adsantos --create-namespace cert-app ./helm
```

## Run with docker

```bash
./start.sh
```

## Run locally

```bash
cd app

./start.sh
```

## Testing

### local / docker

```bash
wget --content-disposition http://localhost:5000/adsantos/cert-app/get-cert?p=anderson
```

### k8s

```bash
#export EXTERNAL_IP=$(kubectl get svc/ingress-nginx-controller -n ingress-nginx -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')
export EXTERNAL_IP=$(kubectl get ingress/cert-app -n adsantos -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')

wget --content-disposition --header "Host: learn.adsantos.io" http://$EXTERNAL_IP/adsantos/cert-app/get-cert?p=anderson
```

> locahost (for docker desktop) and public ip for cluster in the cloud.

### Browser

For localhost, add to `/etc/hosts`:

```hosts
127.0.0.1   learn.adsantos.io
```

And go to <http://learn.adsantos.io/adsantos/front-app/get-cert?p=anderson>

```bash
open http://learn.adsantos.io/adsantos/cert-app/get-cert?p=anderson
```
