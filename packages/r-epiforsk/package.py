# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpiforsk(RPackage):
	"""Code Sharing at the Department of Epidemiological Research at
Statens Serum Institut

	This is a collection of assorted functions and examples collected 
    from various projects. Currently we have functionalities for simplifying 
    overlapping time intervals, Charlson comorbidity score constructors for 
    Danish data, sibling design linear regression functionalities, and a method 
    for calculating the confidence intervals for functions of parameters from a 
    GLM.
	"""
	
	cran = "EpiForsk" 

	version("0.0.1", md5="a9973b3a55e597f6c498bc1313c63158")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
