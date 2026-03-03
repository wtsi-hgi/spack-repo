# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetapower(RPackage):
	"""Power Analysis for Meta-Analysis

	A simple and effective tool for computing and visualizing statistical power for meta-analysis,
    including power analysis of main effects (Jackson & Turner, 2017)<doi:10.1002/jrsm.1240>, 
    test of homogeneity (Pigott, 2012)<doi:10.1007/978-1-4614-2278-5>, subgroup analysis, 
    and categorical moderator analysis (Hedges & Pigott, 2004)<doi:10.1037/1082-989X.9.4.426>.
	"""
	
	cran = "metapower" 

	version("0.2.2", md5="e83c5a9a18cf68f40062583818e64cc2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cowplot@1:", type=("build", "run"))
	depends_on("r-dplyr@0.8.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-knitr@1.28:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-tidyr@1.0.2:", type=("build", "run"))
	depends_on("r-testthat@2.3.2:", type=("build", "run"))
	depends_on("r-rlang@0.4.5:", type=("build", "run"))
