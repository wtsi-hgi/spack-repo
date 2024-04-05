# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMade4(RPackage):
	"""Multivariate analysis of microarray data using ADE4

	Multivariate data analysis and graphical display of microarray data. Functions include for supervised dimension reduction (between group analysis) and joint dimension reduction of 2 datasets (coinertia analysis). It contains functions that require R package ade4.
	"""
	
	homepage = "http://www.hsph.harvard.edu/aedin-culhane/"
	bioc = "made4" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/made4_1.76.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/made4/made4_1.76.0.tar.gz"]

	version("1.76.0", md5="ae8a8a420c5f5ebd8a729767baf0a762", url="https://www.bioconductor.org/packages/release/bioc/src/contrib/made4_1.76.0.tar.gz")
	version("1.76.0", md5="ae8a8a420c5f5ebd8a729767baf0a762", url="https://www.bioconductor.org/packages/3.18/bioc/src/contrib/made4_1.76.0.tar.gz")

	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
