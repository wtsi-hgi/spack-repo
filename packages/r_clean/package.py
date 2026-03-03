# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClean(RPackage):
	"""Fast and Easy Data Cleaning

	A wrapper around the new 'cleaner' package, that allows
  data cleaning functions for classes 'logical', 'factor', 'numeric', 
  'character', 'currency' and 'Date' to make data cleaning fast and
  easy. Relying on very few dependencies, it provides smart guessing,
  but with user options to override anything if needed.
	"""
	
	homepage = "https://github.com/msberends/cleaner"
	cran = "clean" 

	version("2.0.0", md5="5da3a470c30b18a45d49cf9b40dcc3ae")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-cleaner@1.2:", type=("build", "run"))
