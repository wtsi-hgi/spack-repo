# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REbimage(RPackage):
	"""Image processing and analysis toolbox for R

	EBImage provides general purpose functionality for image processing and analysis. In the context of (high-throughput) microscopy-based cellular assays, EBImage offers tools to segment cells and extract quantitative cellular descriptors. This allows the automation of such tasks using the R programming language and facilitates the use of other tools in the R environment for signal processing, statistical modeling, machine learning and visualization with image data.
	"""
	
	homepage = "https://github.com/aoles/EBImage"
	bioc = "EBImage" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/EBImage_4.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/EBImage/EBImage_4.44.0.tar.gz"]

	version("4.44.0", sha256="1ebeda2a0a718a8655613e672b6cbaa5592d0cf0dad0b1fa2094964d2c2bb149")

	depends_on("r-biocgenerics@0.7.1:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-tiff", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-fftwtools@0.9.7:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
