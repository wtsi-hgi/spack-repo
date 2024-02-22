# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROcs4r(RPackage):
	"""Interface to Open Collaboration Services (OCS) REST API

	Provides an Interface to Open Collaboration Services 'OCS' (<https://www.open-collaboration-services.org/>) REST API.
	"""
	
	homepage = "https://github.com/eblondel/ocs4R"
	cran = "ocs4R" 

	version("0.2-3", md5="1b63a68a092dc9b495b04d0e2b1b3f51")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-keyring", type=("build", "run"))
