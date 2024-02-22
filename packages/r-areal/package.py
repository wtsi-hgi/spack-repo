# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAreal(RPackage):
	"""Areal Weighted Interpolation

	A pipeable, transparent implementation of areal weighted interpolation
    with support for interpolating multiple variables in a single function call.
    These tools provide a full-featured workflow for validation and estimation
    that fits into both modern data management (e.g. tidyverse) and spatial 
    data (e.g. sf) frameworks.
	"""
	
	homepage = "https://chris-prener.github.io/areal/"
	cran = "areal" 

	version("0.1.8", md5="d418d427fcf433b77a98cc119ce819ba")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
