const readlineSync = require("readline-sync");
const grpc = require("@grpc/grpc-js");
// const grpc = require("grpc");
var protoLoader = require("@grpc/proto-loader");
const PROTO_PATH = "../protocol_buffers/server.proto";

const options = {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
};

var packageDefinition = protoLoader.loadSync(PROTO_PATH,options);
const GradesManager = grpc.loadPackageDefinition(packageDefinition).GradesManager;


var host = '127.0.0.1';
// var port = readlineSync.question("Informe a Porta para conexão: ");
var port = 50051
const client = new GradesManager(
  "localhost:50051",
  grpc.credentials.createInsecure()
);

module.exports = client;