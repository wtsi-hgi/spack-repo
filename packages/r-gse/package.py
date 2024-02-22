# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGse(RPackage):
	"""Robust Estimation in the Presence of Cellwise and Casewise
Contamination and Missing Data

	Robust Estimation of Multivariate Location and Scatter in the
        Presence of Cellwise and Casewise Contamination and Missing Data.
	"""
	
	cran = "GSE" 

	version("4.2-1", md5="1bace2bd11276245dba1cc9e5f60d0ab")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rrcov", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-cellwise", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
