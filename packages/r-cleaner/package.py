# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCleaner(RPackage):
	"""Fast and Easy Data Cleaning

	Data cleaning functions for classes logical,
  factor, numeric, character, currency and Date to make
  data cleaning fast and easy. Relying on very few dependencies, it 
  provides smart guessing, but with user options to override 
  anything if needed.
	"""
	
	homepage = "https://msberends.github.io/cleaner/"
	cran = "cleaner" 

	version("1.5.4", md5="cadd5b6348d85af9faa1b98e681d23c5")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-backports", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-rlang@0.3.1:", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
