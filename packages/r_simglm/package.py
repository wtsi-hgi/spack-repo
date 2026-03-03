# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimglm(RPackage):
	"""Simulate Models Based on the Generalized Linear Model

	Simulates regression models,
    including both simple regression and generalized linear mixed
    models with up to three level of nesting. Power simulations that are
    flexible allowing the specification of missing data, unbalanced designs,
    and different random error distributions are built into the package.
	"""
	
	homepage = "https://github.com/lebebr01/simglm"
	cran = "simglm" 

	version("0.8.9", md5="d741c10d294f4411d696df379c4e5e96")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
