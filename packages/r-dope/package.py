# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDope(RPackage):
	"""Drug Ontology Parsing Engine

	Provides information on drug names (brand, 
    generic and street) for drugs tracked by the DEA. There are functions that 
    will search synonyms and return the drug names and types. The vignettes 
    have extensive information on the work done to create the data for the package.
	"""
	
	homepage = "https://ctn-0094.github.io/DOPE/"
	cran = "DOPE" 

	version("2.1.0", md5="fe7163e52be720952ec32cfa93a17565")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
