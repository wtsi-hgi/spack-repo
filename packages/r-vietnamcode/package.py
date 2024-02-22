# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVietnamcode(RPackage):
	"""Convert Vietnam Provincial Codes

	Converts Vietnam's provinces' names and ID
    across different formats. Handles diacritics and different spellings.
	"""
	
	cran = "vietnamcode" 

	version("0.1.1", md5="176fb765e04991cae5d02e1ce6f06faa")

	depends_on("r@3.1:", type=("build", "run"))
