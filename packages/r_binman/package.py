# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinman(RPackage):
	"""A Binary Download Manager

	Tools and functions for managing the download of binary files.
    Binary repositories are defined in 'YAML' format. Defining new 
    pre-download, download and post-download templates allow additional 
    repositories to be added.
	"""
	
	homepage = "https://docs.ropensci.org/binman/"
	cran = "binman" 

	version("0.1.3", md5="3a1db22bc85c34d55a7d625ca655990b")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-semver", type=("build", "run"))
