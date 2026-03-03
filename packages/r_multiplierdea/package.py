# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiplierdea(RPackage):
	"""Multiplier Data Envelopment Analysis and Cross Efficiency

	Functions are provided for calculating efficiency using multiplier DEA (Data Envelopment Analysis): Measuring the efficiency of decision making units (Charnes et al., 1978 <doi:10.1016/0377-2217(78)90138-8>) and cross efficiency using single and two-phase approach. In addition, it includes some datasets for calculating efficiency and cross efficiency.
	"""
	
	cran = "MultiplierDEA" 

	version("0.1.19", md5="ff13ea1841d777aa7905df400b99e985")

	depends_on("r-lpsolveapi", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-roi", type=("build", "run"))
	depends_on("r-roi-plugin-glpk", type=("build", "run"))
	depends_on("r-ompr", type=("build", "run"))
	depends_on("r-ompr-roi", type=("build", "run"))
