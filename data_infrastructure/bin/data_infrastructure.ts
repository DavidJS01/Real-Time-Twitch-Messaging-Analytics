#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from '@aws-cdk/core';
import { StorageStack, StreamStack } from '../lib/data_infrastructure-stack';
import { sys } from 'typescript';
import {config} from 'dotenv'
import { Stream } from 'stream';

const dotenv = config()

function fatal(error_message:string){
  console.error(error_message);
  sys.exit();
  return undefined // change this later for the env variables
}

const CDK_ACCOUNT = process.env.CDK_ACCOUNT_DEFAULT
const CDK_REGION = process.env.CDK_REGION_DEFAULT

if(CDK_ACCOUNT == undefined){
  fatal("No account specified!")
}

if(CDK_REGION == undefined){
  fatal("No region specified!")
}

const app = new cdk.App();


new StorageStack(app, 'StorageStack');
new StreamStack(app, 'StreamStack');

app.synth()