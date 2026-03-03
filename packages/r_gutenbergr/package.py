# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGutenbergr(RPackage):
	"""Download and Process Public Domain Works from Project Gutenberg

	Download and process public domain works in the Project
    Gutenberg collection <https://www.gutenberg.org/>. Includes metadata for
    all Project Gutenberg works, so that they can be searched and retrieved.
	"""
	
	homepage = "https://docs.ropensci.org/gutenbergr/"
	cran = "gutenbergr" 

	version("0.2.4", md5="e6249c42bea7eaeba8957d2a9da238d2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
