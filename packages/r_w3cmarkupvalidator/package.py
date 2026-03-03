# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RW3cmarkupvalidator(RPackage):
	"""R Interface to W3C Markup Validation Services

	
  R interface to a W3C Markup Validation service.
  See <https://validator.w3.org/> for more information.
	"""
	
	cran = "W3CMarkupValidator" 

	version("0.1-7", md5="efea1bd565942282849331463a435ac9")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
