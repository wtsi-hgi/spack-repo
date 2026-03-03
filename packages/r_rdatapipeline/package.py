# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdatapipeline(RPackage):
	"""Functions to Interact with the 'FAIR Data Pipeline'

	R implementation of the 'FAIR Data Pipeline API'. The 'FAIR Data 
    Pipeline' is intended to enable tracking of provenance of FAIR (findable, 
    accessible and interoperable) data used in epidemiological modelling.
	"""
	
	homepage = "https://www.fairdatapipeline.org/rDataPipeline/"
	cran = "rDataPipeline" 

	version("0.54.1", md5="1cfb343af918fcc77780563f7d88c6c7")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-configr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-git2r", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-semver", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
