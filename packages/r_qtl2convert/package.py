# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQtl2convert(RPackage):
	"""Convert Data among QTL Mapping Packages

	Functions to convert data structures among the 'qtl2', 'qtl', and 'DOQTL' packages for mapping quantitative trait loci (QTL).
	"""
	
	homepage = "https://kbroman.org/qtl2/"
	cran = "qtl2convert" 

	version("0.28", md5="65c2a34f9e2dfccaadbdce05811b8032")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-qtl@1.40.8:", type=("build", "run"))
	depends_on("r-qtl2@0.18:", type=("build", "run"))
