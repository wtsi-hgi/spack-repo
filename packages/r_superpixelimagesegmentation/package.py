# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSuperpixelimagesegmentation(RPackage):
	"""Superpixel Image Segmentation

	Image Segmentation using Superpixels, Affinity Propagation and Kmeans Clustering. The R code is based primarily on the article "Image Segmentation using SLIC Superpixels and Affinity Propagation Clustering, Bao Zhou, International Journal of Science and Research (IJSR), 2013" <https://www.ijsr.net/archive/v4i4/SUB152869.pdf>. 
	"""
	
	homepage = "https://github.com/mlampros/SuperpixelImageSegmentation"
	cran = "SuperpixelImageSegmentation" 

	version("1.0.5", md5="55ebf6170d6a5ff21acab8346830e3a4")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-openimager", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.1:", type=("build", "run"))
	depends_on("r-clusterr", type=("build", "run"))
