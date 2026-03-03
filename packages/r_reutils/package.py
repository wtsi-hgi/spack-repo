# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReutils(RPackage):
	"""Talk to the NCBI EUtils

	An interface to NCBI databases such as PubMed, GenBank, or GEO
    powered by the Entrez Programming Utilities (EUtils). The nine EUtils
    provide programmatic access to the NCBI Entrez query and database
    system for searching and retrieving biological data.
	"""
	
	homepage = "https://github.com/gschofl/reutils"
	cran = "reutils" 

	version("0.2.3", md5="e0facafc014168c72be3526eb46efa32")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-tibble@1.2:", type=("build", "run"))
