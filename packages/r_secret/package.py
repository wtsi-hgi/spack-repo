# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSecret(RPackage):
	"""Share Sensitive Information in R Packages

	Allow sharing sensitive information, for example passwords,
    'API' keys, etc., in R packages, using public key cryptography.
	"""
	
	homepage = "https://github.com/gaborcsardi/secret#readme"
	cran = "secret" 

	version("1.1.0", md5="fada2e4b619f9bf933ae1c1a19807c43")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-rprojroot", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
