# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RValidatesuggest(RPackage):
	"""Generate Suggestions for Validation Rules

	Generate suggestions for validation rules 
  from a reference data set, which can be used as a starting point for domain specific 
   rules to be checked with package 'validate'.
	"""
	
	homepage = "https://github.com/data-cleaning/validatesuggest"
	cran = "validatesuggest" 

	version("0.3.2", md5="0ca360e85c257efb6857d82754185cb6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-validate", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
