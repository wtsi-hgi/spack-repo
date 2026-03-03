# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesian(RPackage):
	"""Bindings for Bayesian TidyModels

	Fit Bayesian models using 'brms'/'Stan' with 'parsnip'/'tidymodels'
    via 'bayesian' <doi:10.5281/zenodo.6654386>. 'tidymodels' is a collection of
    packages for machine learning; see Kuhn and Wickham (2020) <https://www.tidymodels.org>).
    The technical details of 'brms' and 'Stan' are described in Bürkner (2017)
    <doi:10.18637/jss.v080.i01>, Bürkner (2018) <doi:10.32614/RJ-2018-017>,
    and Carpenter et al. (2017) <doi:10.18637/jss.v076.i01>.
	"""
	
	homepage = "https://hsbadr.github.io/bayesian/"
	cran = "bayesian" 

	version("0.0.9", md5="7ba2ad6fbfc780a5cfd6db1f987e0608")

	depends_on("r-brms@2.17:", type=("build", "run"))
	depends_on("r-parsnip@1:", type=("build", "run"))
	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
