# cdktf-cloudflare-workers-kv-namespace

CDKTF app that deploys a Workers KV namespace to Cloudflare.

## Prerequisites

For this project you need a Cloudflare account.

## Installation

Install CDKTF:

```sh
npm install -g cdktf
```

Install Poetry + dotenv plugin:

```sh
curl -sSL https://install.python-poetry.org | python3 -
poetry self add poetry-plugin-dotenv
```

Configure Poetry to create the virtualenv inside the project's root directory:

```sh
poetry config virtualenvs.in-project true
```

Create the virtualenv and install all the dependencies inside it:

```sh
poetry install
```

## Configuration

In order to deploy to Cloudflare, you need to [create an API Token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) using the `Edit Cloudflare Workers` template.

After that, rename `.env.example` to `.env` and add your variables like in the following example:

```dotenv
CLOUDFLARE_ACCOUNT_ID=0123456789abcdef0123456789abcdef
CLOUDFLARE_API_TOKEN=_ABCDEF_0123456789abcdef0123456789abcdef
```

## Deployment

Synthesize the Terraform stack and deploy it:

```sh
cdktf deploy
```

## Cleanup

Destroy the Terraform stack:

```sh
cdktf destroy
```
