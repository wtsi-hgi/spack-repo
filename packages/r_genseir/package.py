# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenseir(RPackage):
	"""Predict Epidemic Curves with Generalized SEIR Modeling

	Performs generalized Susceptible-Exposed-Infected-Recovered (SEIR) modeling to predict epidemic curves. The method is described in Peng et al. (2020) <doi:10.1101/2020.02.16.20023465>.
	"""
	
	cran = "genSEIR" 

	version("0.1.1", md5="338a8d8d5ab66262b3648efab34c29f3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-nlsr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
