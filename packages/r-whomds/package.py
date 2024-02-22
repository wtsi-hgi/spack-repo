# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWhomds(RPackage):
	"""Calculate Results from WHO Model Disability Survey Data

	The Model Disability Survey (MDS) <https://www.who.int/activities/collection-of-data-on-disability> is a World Health Organization (WHO) general population survey
    instrument to assess the distribution of disability within a country or 
    region, grounded in the International Classification of Functioning, 
    Disability and Health <https://www.who.int/standards/classifications/international-classification-of-functioning-disability-and-health>. This package provides fit-for-purpose functions 
    for calculating and presenting the results from this survey, as used by 
    the WHO. The package primarily provides functions for implementing
    Rasch Analysis (see Andrich (2011) <doi:10.1586/erp.11.59>) to
    calculate a metric scale for disability.
	"""
	
	homepage = "https://github.com/lindsayevanslee/whomds"
	cran = "whomds" 

	version("1.1.1", md5="fb0bb9106e5b96ec6d4b95d968da8fda")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-erm", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gparotation", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-nfactors", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-polycor", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-srvyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tam", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-wrightmap", type=("build", "run"))
