# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTci(RPackage):
	"""Target Controlled Infusion (TCI)

	Implementation of target-controlled infusion algorithms for compartmental pharmacokinetic and pharmacokinetic-pharmacodynamic models. Jacobs (1990) <doi:10.1109/10.43622>; Marsh et al. (1991) <doi:10.1093/bja/67.1.41>; Shafer and Gregg (1993) <doi:10.1007/BF01070999>; Schnider et al. (1998) <doi:10.1097/00000542-199805000-00006>; Abuhelwa, Foster, and Upton (2015) <doi:10.1016/j.vascn.2015.03.004>; Eleveld et al. (2018) <doi:10.1016/j.bja.2018.01.018>.
	"""
	
	homepage = "https://github.com/jarretrt/tci"
	cran = "tci" 

	version("0.2.0", md5="8a2cd64461e7d3fca6e86f09070d401c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
