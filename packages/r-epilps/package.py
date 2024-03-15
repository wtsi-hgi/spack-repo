# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpilps(RPackage):
	"""A Fast and Flexible Bayesian Tool for Estimating Epidemiological
Parameters

	Estimation of epidemiological parameters with 
 Laplacian-P-splines following the methodology of Gressani et al. (2022)
 <doi:10.1371/journal.pcbi.1010618>. 
	"""
	
	homepage = "<https://epilps.com/>"
	cran = "EpiLPS" 

	version("1.3.0", md5="66a55e5c80c6275ba93c3c966f6487d4")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-coda@0.19.4:", type=("build", "run"))
	depends_on("r-epiestim@2.2.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
