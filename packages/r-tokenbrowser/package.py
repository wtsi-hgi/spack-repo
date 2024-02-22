# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTokenbrowser(RPackage):
	"""Create Full Text Browsers from Annotated Token Lists

	Create browsers for reading full texts from a token list format.
    Information obtained from text analyses (e.g., topic modeling, word scaling)
    can be used to annotate the texts.
	"""
	
	cran = "tokenbrowser" 

	version("0.1.5", md5="e4516e019de4cabba9e45561068585e0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
