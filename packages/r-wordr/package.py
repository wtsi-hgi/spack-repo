# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWordr(RPackage):
	"""Rendering Word Documents with R Inline Code

	Serves for rendering MS Word documents with R inline code and inserting tables and plots.
	"""
	
	cran = "WordR" 

	version("0.3.6", md5="da9b9e353bbda917683cf64b818c21f4")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-officer@0.5:", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
