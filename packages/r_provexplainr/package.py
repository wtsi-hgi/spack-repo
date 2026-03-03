# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProvexplainr(RPackage):
	"""Compare Provenance Collections to Explain Changed Script Outputs

	
    Inspects provenance collected by the 'rdt' or 'rdtLite' packages, 
    or other tools providing compatible PROV JSON output created by 
    the execution of a script, and find differences between two provenance 
    collections. Factors under examination included the hardware and 
    software used to execute the script, versions of attached libraries, 
    use of global variables, modified inputs and outputs, and changes 
    in main and sourced scripts. Based on detected changes, 'provExplainR' 
    can be used to study how these factors affect the behavior of 
    the script and generate a promising diagnosis of the causes of different 
    script results. More information about 'rdtLite' and associated tools is available 
    at <https://github.com/End-to-end-provenance/> and Barbara Lerner, 
    Emery Boose, and Luis Perez (2018), Using Introspection to Collect 
    Provenance in R, Informatics, <doi:10.3390/informatics5010012>.
	"""
	
	homepage = "https://github.com/End-to-end-provenance"
	cran = "provExplainR" 

	version("1.1.1", md5="112a656b2fd05f36f97cb5efb2f233ee")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-provparser@0.1.2:", type=("build", "run"))
	depends_on("r-diffobj", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
