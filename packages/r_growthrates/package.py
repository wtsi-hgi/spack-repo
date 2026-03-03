# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrowthrates(RPackage):
	"""Estimate Growth Rates from Experimental Data

	A collection of methods to determine growth rates from
    experimental data, in particular from batch experiments and
    plate reader trials.
	"""
	
	homepage = "https://github.com/tpetzoldt/growthrates"
	cran = "growthrates" 

	version("0.8.4", md5="b92362f8d9953a82556597e136cfc23b")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-fme", type=("build", "run"))
