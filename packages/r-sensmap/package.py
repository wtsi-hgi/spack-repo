# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSensmap(RPackage):
	"""Sensory and Consumer Data Mapping

	Provides Sensory and Consumer Data 
    mapping and analysis <doi:10.14569/IJACSA.2017.081266>. The mapping visualization is made available
    from several features : options in dimension reduction methods and prediction models ranging from 
    linear to non linear regressions. A smoothed version of the map performed using locally weighted regression algorithm 
    is available. A selection process of map stability is provided. A 'shiny' application is included. 
    It presents an easy GUI for the implemented functions as well as a comparative tool of fit models
    using several criteria. Basic analysis such as characterization of products,
    panelists and sessions likewise consumer segmentation are also made available.
	"""
	
	homepage = "https://github.com/IbtihelRebhi/SensMap"
	cran = "SensMap" 

	version("0.7", md5="f35f13f84c8ae8e42b68e6fdd76a3cfd")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-doby", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-factoextra", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-ggdendro", type=("build", "run"))
	depends_on("r-glmulti", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
