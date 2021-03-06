/*
A KBase module: KEHomologyConnector
*/

module KEConnectorGenomeHomology {

    typedef structure {
    	string app_guid;
    	string obj_ref;
    } RunParams;

    typedef structure {
    } RunOutput;

    funcdef run(RunParams params) returns (RunOutput) authentication required;
};
