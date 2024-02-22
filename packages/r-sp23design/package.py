# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSp23design(RPackage):
	"""Design and Simulation of Seamless Phase II-III Clinical Trials

	Provides methods for generating, exploring and executing seamless Phase II-III designs of Lai, Lavori and Shih using generalized likelihood ratio statistics. Includes pdf and source files that describe the entire R implementation with the relevant mathematical details.
	"""
	
	cran = "sp23design" 

	version("0.9-1", md5="244d03cfe4ab68e7d2077a802cd78db6")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
