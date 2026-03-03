# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGtranslate(RPackage):
	"""Translate Between Different Languages

	The goal of this package is to translate between different languages without any Google API authentication which is pain and you must pay for the key, This package is free and lightweight.
	"""
	
	cran = "gtranslate" 

	version("0.0.1", md5="9c93545c61373ee56a11677098730cc2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
