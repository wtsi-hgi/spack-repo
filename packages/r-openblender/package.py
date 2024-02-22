# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpenblender(RPackage):
	"""Request <https://openblender.io> API Services

	Interface to make HTTP requests to 'OpenBlender' API services. Go to <https://openblender.io> for more information.
	"""
	
	cran = "openblender" 

	version("0.5.81", md5="d6e2debafc3112127ce8755cf9893a5b")

	depends_on("r@3.3.3:", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
