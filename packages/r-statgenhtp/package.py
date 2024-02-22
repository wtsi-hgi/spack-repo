# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatgenhtp(RPackage):
	"""High Throughput Phenotyping (HTP) Data Analysis

	Phenotypic analysis of data coming from high throughput 
    phenotyping (HTP) platforms, including different types of outlier detection,
    spatial analysis, and parameter estimation. The package is being developed
    within the EPPN2020 project (<https://eppn2020.plant-phenotyping.eu/>).
    Some functions have been created to be used in conjunction with the R 
    package 'asreml' for the 'ASReml' software, which can be obtained upon 
    purchase from 'VSN' international (<https://vsni.co.uk/software/asreml>).
	"""
	
	homepage = "https://biometris.github.io/statgenHTP/index.html"
	cran = "statgenHTP" 

	version("1.0.6.1", md5="c56ca608920ec9721d0d6107bfdc743f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-animation", type=("build", "run"))
	depends_on("r-factoextra", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-ggnewscale", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-lmmsolver", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-spam", type=("build", "run"))
	depends_on("r-spats@1.0.13:", type=("build", "run"))
