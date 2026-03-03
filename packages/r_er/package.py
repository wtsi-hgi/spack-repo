# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REr(RPackage):
	"""Effect + Residual Modelling

	Multivariate modeling of data after deflation of interfering effects. EF Mosleth et al. (2021) <doi:10.1038/s41598-021-82388-w> and EF Mosleth et al. (2020) <doi:10.1016/B978-0-12-409547-2.14882-6>.
	"""
	
	cran = "ER" 

	version("1.1.1", md5="1ce47368fe3d1ba5a8baa3b05a20a5ff")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-plsvarsel", type=("build", "run"))
