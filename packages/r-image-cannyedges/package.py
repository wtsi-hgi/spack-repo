# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImageCannyedges(RPackage):
	"""Implementation of the Canny Edge Detector for Images

	An implementation of the Canny Edge Detector for detecting edges in images. The package provides an interface to the algorithm available at <https://github.com/Neseb/canny>.
	"""
	
	homepage = "https://github.com/bnosac/image"
	cran = "image.CannyEdges" 

	version("0.1.1", md5="cc9a02cd9f98d35ae74c098a024ec55c")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("libpng", type=("build", "link", "run"))
	depends_on("fftw@3:", type=("build", "link", "run"))
