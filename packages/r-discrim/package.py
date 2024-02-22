# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiscrim(RPackage):
	"""Model Wrappers for Discriminant Analysis

	Bindings for additional classification models for use with
    the 'parsnip' package. Models include flavors of discriminant
    analysis, such as linear (Fisher (1936)
    <doi:10.1111/j.1469-1809.1936.tb02137.x>), regularized (Friedman
    (1989) <doi:10.1080/01621459.1989.10478752>), and flexible (Hastie,
    Tibshirani, and Buja (1994) <doi:10.1080/01621459.1994.10476866>), as
    well as naive Bayes classifiers (Hand and Yu (2007)
    <doi:10.1111/j.1751-5823.2001.tb00465.x>).
	"""
	
	homepage = "https://github.com/tidymodels/discrim"
	cran = "discrim" 

	version("1.0.1", md5="fe754dce7c856aa74fe16c98a9499e45")

	depends_on("r-parsnip@0.2:", type=("build", "run"))
	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dials", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
