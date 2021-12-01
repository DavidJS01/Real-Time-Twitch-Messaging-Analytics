import * as cdk from '@aws-cdk/core';
import * as msk from '@aws-cdk/aws-msk'
// import * as sqs from '@aws-cdk/aws-sqs';
import * as cassandra from '@aws-cdk/aws-cassandra';
import { CfnKeyspace } from '@aws-cdk/aws-cassandra';
import * as ec2 from "@aws-cdk/aws-ec2"


let keyspacething: string = 'CassandraTest_ylGTp6IBx27S'
interface columnProps {
  columnName: string;
  columnType: string;
}


export class StreamStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    const vpc = new ec2.Vpc(this, 'vpcplaceholder', {
      cidr:"placeholder"
    })
    const cluster = new msk.Cluster(this, 'Cluster', {
      clusterName: "clusterplaceholder",
      kafkaVersion: msk.KafkaVersion.V2_8_1,
      vpc,
    });

    cluster.connections.allowFrom(
      ec2.Peer.ipv4("placeholder"),
      ec2.Port.tcp(2181)
    )
    cluster.connections.allowFrom(
      ec2.Peer.ipv4("placeholder"),
      ec2.Port.tcp(9094)
)

  }}

export class StorageStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    

    

    const cfnCassandra = new cassandra.CfnKeyspace(this, 'CassandraTest') // @TODO: explore properties
    const cfnTable = new cassandra.CfnTable(this, "Twitchtv", {
      keyspaceName: keyspacething,
      partitionKeyColumns: [{
        columnName: 'streamkeyplaceholder',
        columnType: "varchar"
      }]
      // regularColumns: [{
      //   columnName: 'Placeholder',
      //   columnType: 'String'
      // }],
    })


  }

}
