# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsmseda(RPackage):
	"""Exploratory Data Analysis of LC-MS/MS data by spectral counts

	Exploratory data analysis to assess the quality of a set of LC-MS/MS experiments, and visualize de influence of the involved factors.
	"""
	
	bioc = "msmsEDA" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/msmsEDA_1.40.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/msmsEDA/msmsEDA_1.40.0.tar.gz"]

	version("1.40.0", md5="d2350677044dfea55c25faa434894cb2")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-msnbase", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
