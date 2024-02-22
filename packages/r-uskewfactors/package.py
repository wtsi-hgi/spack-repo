# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUskewfactors(RPackage):
	"""Model-Based Clustering via Mixtures of Unrestricted Skew-t
Sactor Analyzer Models

	Implements mixtures of unrestricted skew-t factor analyzer models via the EM algorithm.
	"""
	
	cran = "uskewFactors" 

	version("2.0", md5="57eae0d976aeb28e0a5320d97e137b9c")

	depends_on("r-tmvtnorm", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
