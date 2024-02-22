# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTextcat(RPackage):
	"""N-Gram Based Text Categorization

	Text categorization based on n-grams.
	"""
	
	cran = "textcat" 

	version("1.0-8", md5="96da4f9b3270130818ad00aa84b79682")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-tau@0.0.11:", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
