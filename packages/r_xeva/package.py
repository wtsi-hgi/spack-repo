# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXeva(RPackage):
	"""Analysis of patient-derived xenograft (PDX) data

	The Xeva package provides efficient and powerful functions for patient-drived xenograft (PDX) based pharmacogenomic data analysis. This package contains a set of functions to perform analysis of patient-derived xenograft data. This package was developed by the BHKLab, for further information please see our documentation.
	"""
	
	bioc = "Xeva" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Xeva_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Xeva/Xeva_1.18.0.tar.gz"]

	version("1.18.0", md5="94733e069395be524fa2d7254f9c2c5c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-bbmisc", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-rmisc", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-pharmacogx", type=("build", "run"))
	depends_on("r-downloader", type=("build", "run"))
