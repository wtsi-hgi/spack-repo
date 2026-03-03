# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGemtc(RPackage):
	"""Network Meta-Analysis Using Bayesian Methods

	Network meta-analyses (mixed treatment comparisons) in the Bayesian
    framework using JAGS. Includes methods to assess heterogeneity and
    inconsistency, and a number of standard visualizations.
    van Valkenhoef et al. (2012) <doi:10.1002/jrsm.1054>;
    van Valkenhoef et al. (2015) <doi:10.1002/jrsm.1167>.
	"""
	
	homepage = "https://github.com/gertvv/gemtc"
	cran = "gemtc" 

	version("1.0-2", md5="dd3e0771c7ea45d44baab134d4032bd9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-coda@0.13:", type=("build", "run"))
	depends_on("r-igraph@1:", type=("build", "run"))
	depends_on("r-meta@2.1:", type=("build", "run"))
	depends_on("r-plyr@1.8:", type=("build", "run"))
	depends_on("r-rjags@4.0:", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-rglpk", type=("build", "run"))
	depends_on("r-forcats@0.5:", type=("build", "run"))
