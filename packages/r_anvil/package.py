# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnvil(RPackage):
	"""Bioconductor on the AnVIL compute environment

	The AnVIL is a cloud computing resource developed in part by the National Human Genome Research Institute. The AnVIL package provides end-user and developer functionality. For the end-user, AnVIL provides fast binary package installation, utitlities for working with Terra / AnVIL table and data resources, and convenient functions for file movement to and from Google cloud storage. For developers, AnVIL provides programatic access to the Terra, Leonardo, Rawls, and Dockstore RESTful programming interface, including helper functions to transform JSON responses to formats more amenable to manipulation in R.
	"""
	
	bioc = "AnVIL" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/AnVIL_1.14.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/AnVIL/AnVIL_1.14.2.tar.gz"]

	version("1.14.2", md5="43a5cf2e73ee5a400bab98cd756a918c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rapiclient@0.1.3:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
