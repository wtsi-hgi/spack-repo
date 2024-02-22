# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultilevelmod(RPackage):
	"""Model Wrappers for Multi-Level Models

	Bindings for hierarchical regression models for use with the
    'parsnip' package. Models include longitudinal generalized linear
    models (Liang and Zeger, 1986) <doi:10.1093/biomet/73.1.13>, and
    mixed-effect models (Pinheiro and Bates)
    <doi:10.1007/978-1-4419-0318-1_1>.
	"""
	
	homepage = "https://github.com/tidymodels/multilevelmod"
	cran = "multilevelmod" 

	version("1.0.0", md5="b458023b48c8d74b6a3dbe8bbab4ea5e")

	depends_on("r-parsnip@1:", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
