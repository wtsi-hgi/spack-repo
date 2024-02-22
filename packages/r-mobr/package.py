# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMobr(RPackage):
	"""Measurement of Biodiversity

	Functions for calculating metrics for the measurement biodiversity
    and its changes across scales, treatments, and gradients. The methods 
    implemented in this package are described in:
    Chase, J.M., et al. (2018) <doi:10.1111/ele.13151>, 
    McGlinn, D.J., et al. (2019) <doi:10.1111/2041-210X.13102>, and
    McGlinn, D.J., et al. (2021) <doi:10.1002/ecy.3233>. 
	"""
	
	cran = "mobr" 

	version("2.0.2", md5="284d612a6c78fea3e9e7adf727182781")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-egg", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
