# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcrosstic(RPackage):
	"""A Cost-Minimal Regular Spanning Subgraph with TreeClust

	Construct minimum-cost regular spanning subgraph as part of a
    non-parametric two-sample test for equality of distribution.
	"""
	
	cran = "AcrossTic" 

	version("1.0-3", md5="f768c68b8fcf88563482664544175147")

	depends_on("r-treeclust@1.1.6:", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
