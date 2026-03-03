# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDhglm(RPackage):
	"""Double Hierarchical Generalized Linear Models

	Implements double hierarchical generalized linear models in which the mean, dispersion parameters for variance of random effects, and residual variance (overdispersion) can be further modeled as random-effect models.
	"""
	
	cran = "dhglm" 

	version("2.0", md5="aa6df7616640dba6711357d5bb5023e9")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
