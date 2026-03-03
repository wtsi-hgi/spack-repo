# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRavages(RPackage):
	"""Rare Variant Analysis and Genetic Simulations

	Rare variant association tests: burden tests (Bocher et al. 2019 <doi:10.1002/gepi.22210>) and the Sequence Kernel Association Test (Bocher et al. 2021 <doi:10.1038/s41431-020-00792-8>) in the whole genome; and genetic simulations.
	"""
	
	cran = "Ravages" 

	version("1.1.3", md5="877ad7f315fb8ea10ac325e935b92413")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-gaston", type=("build", "run"))
	depends_on("r-mlogit@1.1.0:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-dfidx", type=("build", "run"))
	depends_on("r-bedr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
