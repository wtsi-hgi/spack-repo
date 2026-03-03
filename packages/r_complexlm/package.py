# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComplexlm(RPackage):
	"""Linear Fitting for Complex Valued Data

	Tools for linear fitting with complex variables. Includes ordinary least-squares (zlm()) and robust M-estimation (rzlm()), and complex methods for oft used generics. Originally adapted from the rlm() functions of 'MASS' and the lm() functions of 'stats'.
	"""
	
	homepage = "https://github.com/QuantumOfMoose/complexlm"
	cran = "complexlm" 

	version("1.1.2", md5="e8c05508dc164c9da1ee7408297030de")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
