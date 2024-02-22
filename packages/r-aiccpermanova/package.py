# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAiccpermanova(RPackage):
	"""Model Selection of PERMANOVA Models Using AICc

	Provides tools for model selection and model averaging of PerMANOVA 
    models using Akaike Information Criterion corrected for small sample sizes 
    (AICc) and Information Theoretic criteria principles. The package is built 
    around the PERMANOVA analysis from the 'vegan' package and provides a 
    streamlined workflow for generating and comparing models, obtaining model 
    weights, and summarizing results using model averaging approaches.  The 
    methods implemented in this package are based on the practical information-
    theoretic approach described by Burnham, K. P. and Anderson, D. R. (2002) 
    (<doi:10.1007/b97636>).
	"""
	
	homepage = "https://github.com/Sustainscapes/AICcPerm"
	cran = "AICcPermanova" 

	version("0.0.2", md5="dea4b1d7f443bf6a3450a41e2021ac99")

	depends_on("r-broom", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
