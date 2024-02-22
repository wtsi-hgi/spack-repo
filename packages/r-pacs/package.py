# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPacs(RPackage):
	"""Supplementary Tools for R Packages Developers

	
  Supplementary utils for CRAN maintainers and R packages developers.
  Validating the library, packages and lock files.
  Exploring a complexity of a specific package like evaluating its size in bytes with all dependencies.
  The shiny app complexity could be explored too.
  Assessing the life duration of a specific package version.
  Checking a CRAN package check page status for any errors and warnings.
  Retrieving a DESCRIPTION or NAMESPACE file for any package version. 
  Comparing DESCRIPTION or NAMESPACE files between different package versions.
  Getting a list of all releases for a specific package.
  The Bioconductor is partly supported.
	"""
	
	homepage = "https://github.com/Polkas/pacs"
	cran = "pacs" 

	version("0.5.1", md5="98259bf489f0097e18e6fe3d0d9c65d8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
