# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLtmle(RPackage):
	"""Longitudinal Targeted Maximum Likelihood Estimation

	Targeted Maximum Likelihood Estimation ('TMLE') of
    treatment/censoring specific mean outcome or marginal structural model for
    point-treatment and longitudinal data.
	"""
	
	homepage = "https://github.com/joshuaschwab/ltmle"
	cran = "ltmle" 

	version("1.3-0", md5="c74e7aede9b24815d5d841768ce0e3d6")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
