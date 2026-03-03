# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCeoptim(RPackage):
	"""Cross-Entropy R Package for Optimization

	Optimization solver based on the Cross-Entropy method.
	"""
	
	cran = "CEoptim" 

	version("1.3", md5="b1900a2c48f996ecc16d8a05eacc2a0e")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
