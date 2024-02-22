# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCp(RPackage):
	"""Conditional Power Calculations

	Functions for calculating the conditional power
             for different models in survival time analysis
             within randomized clinical trials
             with two different treatments to be compared
             and survival as an endpoint.
	"""
	
	homepage = "https://www.genstat.imise.uni-leipzig.de/"
	cran = "CP" 

	version("1.8", md5="3e415a89345fde37c365755f571e57e1")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
