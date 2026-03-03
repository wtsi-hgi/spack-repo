# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAvailable(RPackage):
	"""Check if the Title of a Package is Available, Appropriate and
Interesting

	Check if a given package name is available to use. It checks the
  name's validity. Checks if it is used on 'GitHub', 'CRAN' and 'Bioconductor'. Checks
  for unintended meanings by querying 'Wiktionary' and Wikipedia.
	"""
	
	homepage = "https://github.com/r-lib/available"
	cran = "available" 

	version("1.1.0", md5="0d386b8c09c146a96f46aaaf9f5b3c04")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-clisymbols", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
	depends_on("r-desc", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-snowballc", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-yesno", type=("build", "run"))
