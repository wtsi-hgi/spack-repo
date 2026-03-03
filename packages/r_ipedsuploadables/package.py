# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpedsuploadables(RPackage):
	"""Transforms Institutional Data into Text Files for IPEDS
Automated Import/Upload

	Starting from user-supplied institutional data, these scripts 
    transform, aggregate, and reshape the information to produce 
    key-value pair data files that are able to be uploaded to IPEDS (Integrated Postsecondary Education Data System) 
    through their submission portal <https://surveys.nces.ed.gov/ipeds/>. Starting data specifications can be found in the vignettes.  
    Final files are saved locally to a location of the user's choice. 
    User-friendly readable files can also be produced for purposes of data review and validation. 
	"""
	
	homepage = "https://github.com/AlisonLanski/IPEDSuploadables"
	cran = "IPEDSuploadables" 

	version("2.8.7", md5="cfd5e9ff20cec0105936baf8275d49a6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-svdialogs", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
