# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBroomMixed(RPackage):
	"""Tidying Methods for Mixed Models

	Convert fitted objects from various R mixed-model packages
    into tidy data frames along the lines of the 'broom' package.
    The package provides three
    S3 generics for each model: tidy(), which summarizes a model's statistical findings such as
    coefficients of a regression; augment(), which adds columns to the original
    data such as predictions, residuals and cluster assignments; and glance(), which
    provides a one-row summary of model-level statistics.
	"""
	
	homepage = "https://github.com/bbolker/broom.mixed"
	cran = "broom.mixed" 

	version("0.2.9.4", md5="9209667d92aab58a673fc8decab1a276")
	version("0.2.9.5", md5="dcabde69bdf16a16c047552e47aa5b91")

	depends_on("r-broom", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
