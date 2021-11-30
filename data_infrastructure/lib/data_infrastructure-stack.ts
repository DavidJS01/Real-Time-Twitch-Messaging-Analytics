import * as cdk from '@aws-cdk/core';
// import * as sqs from '@aws-cdk/aws-sqs';
import * as cassandra from '@aws-cdk/aws-cassandra';
import { CfnKeyspace } from '@aws-cdk/aws-cassandra';

let keyspacething: string = 'CassandraTest_ylGTp6IBx27S'
interface columnProps {
  columnName: string;
  columnType: string;
}

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
