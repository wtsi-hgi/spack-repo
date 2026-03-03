# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStriprtf(RPackage):
	"""Extract Text from RTF File

	Extracts plain text from RTF (Rich Text Format) file.
	"""
	
	homepage = "https://github.com/kota7/striprtf"
	cran = "striprtf" 

	version("0.6.0", md5="6326307325889f30aa70522f1045a288")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
