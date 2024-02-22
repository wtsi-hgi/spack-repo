# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPepsnmr(RPackage):
	"""Pre-process 1H-NMR FID signals

	This package provides R functions for common pre-procssing steps that are applied on 1H-NMR data. It also provides a function to read the FID signals directly in the Bruker format.
	"""
	
	homepage = "https://github.com/ManonMartin/PepsNMR"
	bioc = "PepsNMR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/PepsNMR_1.20.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/PepsNMR/PepsNMR_1.20.0.tar.gz"]

	version("1.20.0", md5="afd34a264a3af86ad7aec1d6163b0aab")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ptw", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
