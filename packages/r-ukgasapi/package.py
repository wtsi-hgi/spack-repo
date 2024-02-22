# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUkgasapi(RPackage):
	"""API for UK Energy Market Information

	Allows users to access live UK energy market information via various APIs.
	"""
	
	cran = "ukgasapi" 

	version("0.21", md5="8e3a386f6677e3b2f4774631a19b8469")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
