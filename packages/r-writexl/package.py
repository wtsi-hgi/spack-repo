# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWritexl(RPackage):
	"""Export Data Frames to Excel 'xlsx' Format

	Zero-dependency data frame to xlsx exporter based on 'libxlsxwriter'. 
    Fast and no Java or Excel required.
	"""
	
	homepage = "https://docs.ropensci.org/writexl/"
	cran = "writexl" 

	version("1.5.0", md5="17dacf647864aed0b745bdd174601b4c")

	depends_on("zlib", type=("build", "link", "run"))
	depends_on("zlib", type=("build", "link", "run"))
