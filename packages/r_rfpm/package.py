# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfpm(RPackage):
	"""Floating Percentile Model

	Floating Percentile Model with additional functions for optimizing inputs and evaluating outputs and assumptions.
	"""
	
	cran = "RFPM" 

	version("1.1", md5="a675147f48e8923af963821a8c590bb3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lawstat", type=("build", "run"))
