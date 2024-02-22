# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCg(RPackage):
	"""Compare Groups, Analytically and Graphically

	Comprehensive data analysis software, and the name "cg" stands for "compare groups." Its genesis and evolution are driven by common needs to compare administrations, conditions, etc. in medicine research and development. The current version provides comparisons of unpaired samples, i.e. a linear model with one factor of at least two levels. It also provides comparisons of two paired samples. Good data graphs, modern statistical methods, and useful displays of results are emphasized.
	"""
	
	cran = "cg" 

	version("1.0-3", md5="a1329961d2f7dc71b02fecc2ff47f60c")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-hmisc@3.17.1:", type=("build", "run"))
	depends_on("r-vgam@1.0.0:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
