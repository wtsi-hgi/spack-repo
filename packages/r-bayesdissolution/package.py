# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesdissolution(RPackage):
	"""Bayesian Models for Dissolution Testing

	Fits Bayesian models (amongst others) to dissolution data sets that can be used for dissolution testing. The package was originally constructed to include only the Bayesian models outlined in Pourmohamad et al. (2022) <doi:10.1111/rssc.12535>. However, additional Bayesian and non-Bayesian models (based on bootstrapping and generalized pivotal quanties) have also been added. More models may be added over time.
	"""
	
	cran = "BayesDissolution" 

	version("0.2.0", md5="30f076dbeea84327650b64cff3396bdb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-geor", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-pscl", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
