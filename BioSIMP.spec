/*
A KBase module: BioSIMP
*/

module BioSIMP {
    /*
        Insert your typespec information here.
    */

	
	typedef structure{
		string workspace_name;
		string fbamodel_id;
		string media;
		string fbaOuptut_id;
	}BioSIMPParams;

	typedef structure{
		string report_name;
		string report_ref;
	}BioSIMPOutput;

	funcdef BioSIMP(BioSIMPParams params) returns (BioSIMPOutput) authentication required;

};
