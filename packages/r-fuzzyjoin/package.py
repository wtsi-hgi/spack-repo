# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuzzyjoin(RPackage):
	"""Join Tables Together on Inexact Matching

	Join tables together based not on whether columns
  match exactly, but whether they are similar by some comparison.
  Implementations include string distance and regular expression
  matching.
	"""
	
	homepage = "https://github.com/dgrtwo/fuzzyjoin"
	cran = "fuzzyjoin" 

	version("0.1.6", md5="d472d77dec7889760a9323a90aacc89e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr@0.8.1:", type=("build", "run"))
	depends_on("r-tidyr@0.4:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
