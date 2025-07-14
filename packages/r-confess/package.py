# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConfess(RPackage):
	"""Cell OrderiNg by FluorEScence Signal

	Single Cell Fluidigm Spot Detector.
	"""
	
	bioc = "CONFESS" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CONFESS_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CONFESS/CONFESS_1.30.0.tar.gz"]

	version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="828fe6d1f451eb970e30291c04a766f7a7c60e6cbece1f6ab118abb3e2c3941e")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-changepoint", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-contrast", type=("build", "run"))
	depends_on("r-data-table@1.9.7:", type=("build", "run"))
	depends_on("r-ecp", type=("build", "run"))
	depends_on("r-ebimage", type=("build", "run"))
	depends_on("r-flexmix", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-flowclust", type=("build", "run"))
	depends_on("r-flowmeans", type=("build", "run"))
	depends_on("r-flowmerge", type=("build", "run"))
	depends_on("r-flowpeaks", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-outliers", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-readbitmap", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-samspectral", type=("build", "run"))
	depends_on("r-waveslim", type=("build", "run"))
	depends_on("r-wavethresh", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
