# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDesirability2(RPackage):
	"""Desirability Functions for Multiparameter Optimization

	In-line functions for multivariate optimization via desirability 
    functions (Derringer and Suich, 1980, <doi:10.1080/00224065.1980.11980968>)
    with easy use within 'dplyr' pipelines.
	"""
	
	homepage = "https://desirability2.tidymodels.org"
	cran = "desirability2" 

	version("0.0.1", md5="3e164176c4bb83b710ef9fdd96e34389", url="https://cran.r-project.org/src/contrib/desirability2_0.0.1.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
