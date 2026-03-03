# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdditive(RPackage):
	"""Bindings for Additive TidyModels

	Fit Generalized Additive Models (GAM) using 'mgcv' with 'parsnip'/'tidymodels'
    via 'additive' <doi:10.5281/zenodo.6654298>. 'tidymodels' is a collection of
    packages for machine learning; see Kuhn and Wickham (2020) <https://www.tidymodels.org>).
    The technical details of 'mgcv' are described in Wood (2017)
    <doi:10.1201/9781315370279>.
	"""
	
	homepage = "https://hsbadr.github.io/additive/"
	cran = "additive" 

	version("0.0.5", md5="c29f41153f1238caa23a19a04f39d8e1")

	depends_on("r-mgcv@1.8.40:", type=("build", "run"))
	depends_on("r-parsnip@1:", type=("build", "run"))
	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
