# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModeldata(RPackage):
	"""Data Sets Useful for Modeling Examples

	Data sets used for demonstrating or testing model-related
    packages are contained in this package.
	"""
	
	homepage = "https://modeldata.tidymodels.org"
	cran = "modeldata" 

	version("1.3.0", md5="3a8fe77fd64aff48602fa25f049ba330")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
