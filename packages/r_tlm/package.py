# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTlm(RPackage):
	"""Effects under Linear, Logistic and Poisson Regression Models
with Transformed Variables

	Computation of effects under linear, logistic and Poisson regression models with transformed variables. Logarithm and power transformations are allowed. Effects can be displayed both numerically and graphically in both the original and the transformed space of the variables.
	"""
	
	cran = "tlm" 

	version("0.1.5", md5="09684864e10aa167fb78a50830a830c3")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
