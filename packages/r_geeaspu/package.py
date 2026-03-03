# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeeaspu(RPackage):
	"""Adaptive Association Tests for Multiple Phenotypes using
Generalized Estimating Equations (GEE)

	Provides adaptive association tests for SNP level, gene level and pathway level analyses.
	"""
	
	cran = "GEEaSPU" 

	version("1.0.2", md5="9fc1d1605383de775f922429b458f07c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gee", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
