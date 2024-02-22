# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInteractionr(RPackage):
	"""Full Reporting of Interaction Analyses

	Produces a publication-ready table that includes all effect estimates necessary for full reporting effect modification and interaction analysis as recommended by Knol and Vanderweele (2012) [<doi:10.1093/ije/dyr218>]. It also estimates confidence interval for the trio of additive interaction measures using the delta method (see Hosmer and Lemeshow (1992), [<doi:10.1097/00001648-199209000-00012>]), variance recovery method (see Zou (2008), [<doi:10.1093/aje/kwn104>]), or percentile bootstrapping (see Assmann et al. (1996), [<doi:10.1097/00001648-199605000-00012>]). 
	"""
	
	homepage = "https://github.com/tunsmart/interactionR"
	cran = "interactionR" 

	version("0.1.7", md5="a7b72b7ff735a7ee439ae7a5c95d237b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-officer", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
