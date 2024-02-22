# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIweigreg(RPackage):
	"""Improved Methods for Causal Inference and Missing Data Problems

	Improved methods based on inverse probability weighting
        and outcome regression for causal inference and missing data
        problems.
	"""
	
	homepage = "http://www.stat.rutgers.edu/~ztan"
	cran = "iWeigReg" 

	version("1.1", md5="9f107f255e2480cc6e864c03fe1f9529")

	depends_on("r@2.9.1:", type=("build", "run"))
	depends_on("r-mass@7.2.1:", type=("build", "run"))
	depends_on("r-trust", type=("build", "run"))
