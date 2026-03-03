# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGoric(RPackage):
	"""Generalized Order-Restricted Information Criterion

	Generalized Order-Restricted Information Criterion (GORIC) value for a set of hypotheses in multivariate linear models and generalised linear models.
	"""
	
	cran = "goric" 

	version("1.1-2", md5="30e6ca89bea0e0d0c1c505d90c707aca")

	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
