# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultilinguer(RPackage):
	"""Gentle Language Installer for R User

	Provides install functions of other languages 
             such as 'java', 'python'.
	"""
	
	homepage = "https://github.com/mrchypark/multilinguer"
	cran = "multilinguer" 

	version("0.2.4", md5="13e3228952ff3723cb05a6e0964cf7f7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sys", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-askpass", type=("build", "run"))
