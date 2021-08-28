/*
Grpc client configurations files that comunicates with Protobuff server over Protobuff
manage student + grades + enrollment
Authors:
    @MathBatistela
    @mvgolom

Created at: 22/08/2021
Updated at: 23/08/2021
Updated at: 27/08/2021
*/
const readlineSync = require("readline-sync");// library extern readline synchronous
const grpc = require("@grpc/grpc-js");// google Grpc library
var protoLoader = require("@grpc/proto-loader");// protobuff library
const PROTO_PATH = "../protocol_buffers/server.proto";//load proto buffer file config
/*
  Load configs to Grpc
*/
const options = {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
};
/*Define process */
var packageDefinition = protoLoader.loadSync(PROTO_PATH,options);
const GradesManager = grpc.loadPackageDefinition(packageDefinition).GradesManager;

// conection configurations
var host = '127.0.0.1';
var port = 50051
//Start Grpc services
const client = new GradesManager(
  "localhost:50051",
  grpc.credentials.createInsecure()
);

module.exports = client;