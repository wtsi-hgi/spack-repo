# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimpleseg(RPackage):
	"""A package to perform simple cell segmentation

	Image segmentation is the process of identifying the borders of individual objects (in this case cells) within an image. This allows for the features of cells such as marker expression and morphology to be extracted, stored and analysed. simpleSeg provides functionality for user friendly, watershed based segmentation on multiplexed cellular images in R based on the intensity of user specified protein marker channels. simpleSeg can also be used for the normalization of single cell data obtained from multiple images.
	"""
	
	homepage = "https://sydneybiox.github.io/simpleSeg/"
	bioc = "simpleSeg" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/simpleSeg_1.4.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/simpleSeg/simpleSeg_1.4.1.tar.gz"]

	version("1.4.1", md5="bd0a780ed7dfde71db7ecdf2cee30b0c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-ebimage", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-cytomapper", type=("build", "run"))
