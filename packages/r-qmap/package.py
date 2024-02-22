# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQmap(RPackage):
	"""Statistical Transformations for Post-Processing Climate Model
Output

	Empirical adjustment of the distribution of variables originating from (regional) climate model simulations using quantile mapping.
	"""
	
	cran = "qmap" 

	version("1.0-4", md5="70ce6f55142b458c61256598a922c038")

	depends_on("r@2.8:", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
