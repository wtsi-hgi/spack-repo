# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSecsse(RPackage):
	"""Several Examined and Concealed States-Dependent Speciation and
Extinction

	Simultaneously infers state-dependent diversification across
 two or more states of a single or multiple traits while accounting for the
 role of a possible concealed trait. See Herrera-Alsina et al. (2019)
 <doi:10.1093/sysbio/syy057>.  
	"""
	
	homepage = "https://rsetienne.github.io/secsse/"
	cran = "secsse" 

	version("3.0.2", md5="b06250f889b16cbddd79a6cbc1d3cbd9")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-ddd@5:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-geiger", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-bh@1.81.0.1:", type=("build", "run"))
