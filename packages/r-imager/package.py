# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImager(RPackage):
	"""Image Processing Library Based on 'CImg'.

	Fast image processing for images in up to 4 dimensions (two spatial
	dimensions, one time/depth dimension, one colour dimension). Provides most
	traditional image processing tools (filtering, morphology, transformations,
	etc.) as well as various functions for easily analysing image data using R.
	The package wraps 'CImg', <https://cimg.eu/>, a simple, modern C++ library
	for image processing."""

	cran = "imager"

	version("0.45.8", md5="64d32f0539023a7203f7c96cddd42a57")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-readbitmap", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-downloader", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("fftw@3:", type=("build", "link", "run"))
	depends_on("libtiff", type=("build", "link", "run"))
	depends_on("libx11", type=("build", "link", "run"))
