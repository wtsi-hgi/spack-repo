# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTohm(RPackage):
	"""Testing One Hypothesis Multiple Times

	Approximations of global p-values when testing hypothesis in presence of non-identifiable nuisance parameters. The method relies on the Euler characteristic heuristic and the expected Euler characteristic is efficiently computed by  in Algeri and van Dyk (2018) <arXiv:1803.03858>. 
	"""
	
	cran = "TOHM" 

	version("1.4", md5="b62702aded4b3a04cc115bd06c7fd282")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-rmpfr", type=("build", "run"))
	depends_on("r-eql", type=("build", "run"))
