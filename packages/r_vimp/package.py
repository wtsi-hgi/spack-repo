# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVimp(RPackage):
	"""Perform Inference on Algorithm-Agnostic Variable Importance

	Calculate point estimates of and valid confidence intervals for
    nonparametric, algorithm-agnostic variable importance measures in high and low dimensions,
    using flexible estimators of the underlying regression functions. For more information
    about the methods, please see Williamson et al. (Biometrics, 2020),  Williamson et al. (JASA, 2021), and Williamson and Feng (ICML, 2020).
	"""
	
	homepage = "https://bdwilliamson.github.io/vimp/"
	cran = "vimp" 

	version("2.3.3", md5="b42e7cc7e48215f21ff11fd1ad87afba")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-superlearner", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
