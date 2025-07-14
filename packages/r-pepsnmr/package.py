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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/PepsNMR_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/PepsNMR/PepsNMR_1.20.0.tar.gz"]

	version("1.26.0", tag="RELEASE_3_21")
	version("1.20.0", sha256="9c13ecce9310afae0a65c8b45d2427e4ce902c2e786779eb22f2a07c68e27204")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ptw", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
