# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFederalregister(RPackage):
	"""Client Package for the U.S. Federal Register API

	Access data from the Federal Register API <https://www.federalregister.gov/developers/api/v1>.
	"""
	
	homepage = "https://github.com/rOpenGov/federalregister"
	cran = "federalregister" 

	version("0.2.0", md5="72eb7b470baf0895ca68941ea20e302c")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
