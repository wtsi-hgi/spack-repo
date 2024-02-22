# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIgasso(RPackage):
	"""Statistical Tests and Utilities for Genetic Association

	A collection of statistical tests for genetic association studies and summary data based Mendelian randomization.
	"""
	
	cran = "iGasso" 

	version("1.6", md5="f0287051c987aad2c89454101d99210b")

	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mbess", type=("build", "run"))
