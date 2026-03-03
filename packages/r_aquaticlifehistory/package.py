# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAquaticlifehistory(RPackage):
	"""Life History Analysis Tools

	Estimate aquatic species life history using robust techniques.
    This package supports users undertaking two types of analysis: 1) Growth from
    length-at-age data, and 2) maturity analyses for length and/or age data.
    Maturity analyses are performed using generalised linear model approaches incorporating
    either a binomial or quasibinomial distribution.
    Growth modelling is performed using the multimodel approach presented by
    Smart et al. (2016) "Multimodel approaches in shark and ray growth studies:
    strengths, weaknesses and the future" <doi:10.1111/faf.12154>.
	"""
	
	homepage = "https://github.com/jonathansmart/AquaticLifeHistory"
	cran = "AquaticLifeHistory" 

	version("1.0.5", md5="eb7a14e2888fb723699420c6867c9fb8")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-mumin", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
