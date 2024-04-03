# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRirods(RPackage):
	"""R Client for 'iRODS'

	The open sourced data management software 'Integrated
    Rule-Oriented Data System' ('iRODS') offers solutions for the whole
    data life cycle (<https://irods.org/>). The loosely constructed and
    highly configurable architecture of 'iRODS' frees the user from strict
    formatting constraints and single-vendor solutions. This package
    provides an interface to the 'iRODS' HTTP API, allowing you to manage
    your data and metadata in 'iRODS' with R. Storage of annotated files
    and R objects in 'iRODS' ensures findability, accessibility,
    interoperability, and reusability of data.
	"""
	
	homepage = "https://github.com/irods/irods_client_library_rirods"
	cran = "rirods" 

	version("0.2.0", md5="6b3064c6105e2c8025dbd6b7b78ba87e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr2@0.2.2:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-testthat@3:", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
