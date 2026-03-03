# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSdtmval(RPackage):
	"""Validate SDTM Domains

	Provides a set of tools to assist statistical programmers 
    in validating Study Data Tabulation Model (SDTM) domain data sets. 
    Statistical programmers are required to validate that a SDTM data set domain 
    has been programmed correctly, per the SDTM Implementation Guide (SDTMIG) by 
    'CDISC' (<https://www.cdisc.org/standards/foundational/sdtmig>), 
    study specification, and study protocol using a process called double 
    programming. Double programming involves two different programmers 
    independently converting the raw electronic data cut (EDC) data into a SDTM 
    domain data table and comparing their results to ensure accurate 
    standardization of the data. One of these attempts is termed 'production' 
    and the other 'validation'. Generally, production runs are the official 
    programs for submittals and these are written in 'SAS'. Validation runs can 
    be programmed in another language, in this case 'R'. 
	"""
	
	homepage = "https://github.com/skgithub14/sdtmval"
	cran = "sdtmval" 

	version("0.4.1", md5="783c92984707d1d44676c5b5c2cd2686")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
