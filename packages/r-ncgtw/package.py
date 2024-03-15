# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNcgtw(RPackage):
	"""Alignment of LC-MS Profiles by Neighbor-wise Compound-specific Graphical Time Warping with Misalignment Detection

	The purpose of ncGTW is to help XCMS for LC-MS data alignment. Currently, ncGTW can detect the misaligned feature groups by XCMS, and the user can choose to realign these feature groups by ncGTW or not.
	"""
	
	bioc = "ncGTW" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ncGTW_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ncGTW/ncGTW_1.16.0.tar.gz"]

	version("1.16.0", md5="ea33321b03c3751afd04234fd7fbcda3")

	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-xcms", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
