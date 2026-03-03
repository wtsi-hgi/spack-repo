# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvunit(RPackage):
	"""'SciViews' - Unit, Integration and System Testing

	A complete unit test system and functions to implement its GUI part.
	"""
	
	homepage = "https://github.com/SciViews/svUnit"
	cran = "svUnit" 

	version("1.0.6", md5="e8f7bd4037adb70a469f3076f8015e91")

	depends_on("r@1.9:", type=("build", "run"))
