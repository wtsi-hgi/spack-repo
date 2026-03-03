# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSperrorest(RPackage):
	"""Perform Spatial Error Estimation and Variable Importance
Assessment

	Implements spatial error estimation and
    permutation-based variable importance measures for predictive models
    using spatial cross-validation and spatial block bootstrap.
	"""
	
	homepage = "https://giscience-fsu.github.io/sperrorest/"
	cran = "sperrorest" 

	version("3.0.5", md5="abc41e0a471a5d19e7d8209194d80031")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
