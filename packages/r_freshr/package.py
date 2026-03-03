# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFreshr(RPackage):
	"""Make R Environment Fresh Again

	A simple way to unload none-base packages and remove all global
    variables.
	"""
	
	homepage = "https://github.com/shawnlinxl/freshr"
	cran = "freshr" 

	version("1.0.2", md5="9a492d11fa3f8213f4817632000b8a56")

