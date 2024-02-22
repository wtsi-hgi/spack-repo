# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFitdynmix(RPackage):
	"""Estimation of Dynamic Mixtures

	Estimation of a dynamic lognormal - Generalized Pareto mixture via the Approximate Maximum Likelihood and the Cross-Entropy methods. See Bee, M. (2023) <doi:10.1016/j.csda.2023.107764>.
	"""
	
	homepage = "https://github.com/marco-bee/FitDynMix"
	cran = "FitDynMix" 

	version("1.0.0", md5="275860b3783ccd366deee40b45a98f2f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-evir", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
