# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFgeoAnalyze(RPackage):
	"""Analyze ForestGEO Data

	To help you access, transform, analyze, and
    visualize ForestGEO data, we developed a collection of R packages
    (<https://forestgeo.github.io/fgeo/>). This package, in particular,
    helps you to implement analyses of plot species distributions,
    topography, demography, and biomass. It also includes a torus
    translation test to determine habitat associations of tree species as
    described by Zuleta et al. (2018) <doi:10.1007/s11104-018-3878-0>. To
    learn more about ForestGEO visit <https://forestgeo.si.edu/>.
	"""
	
	homepage = "https://github.com/forestgeo/fgeo.analyze"
	cran = "fgeo.analyze" 

	version("1.1.14", md5="c0dcca40a17af1cf500923450d324ac3")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-dplyr@0.8.0.1:", type=("build", "run"))
	depends_on("r-fgeo-tool@1.2.4:", type=("build", "run"))
	depends_on("r-glue@1.3.1:", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-purrr@0.3.2:", type=("build", "run"))
	depends_on("r-rlang@0.3.4:", type=("build", "run"))
	depends_on("r-tibble@2.1.1:", type=("build", "run"))
	depends_on("r-tidyr@0.8.3:", type=("build", "run"))
	depends_on("r-withr@2.1.2:", type=("build", "run"))
