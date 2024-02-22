# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDataverse(RPackage):
	"""Client for Dataverse 4+ Repositories

	Provides access to Dataverse APIs <https://dataverse.org/> (versions 4-5),
    enabling data search, retrieval, and deposit. For Dataverse versions <= 3.0,
    use the archived 'dvn' package <https://cran.r-project.org/package=dvn>.
	"""
	
	homepage = "https://iqss.github.io/dataverse-client-r/"
	cran = "dataverse" 

	version("0.3.13", md5="7ad28461239c47868cd63e3cd83c7e8a")

	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
