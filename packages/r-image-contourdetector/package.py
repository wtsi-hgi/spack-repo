# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImageContourdetector(RPackage):
	"""Implementation of the Unsupervised Smooth Contour Line Detection
for Images

	An implementation of the Unsupervised Smooth Contour Detection algorithm for digital images as described in the paper: "Unsupervised Smooth Contour Detection" by Rafael Grompone von Gioi, and Gregory Randall (2016). 
    The algorithm is explained at <doi:10.5201/ipol.2016.175>.
	"""
	
	homepage = "https://github.com/bnosac/image"
	cran = "image.ContourDetector" 

	version("0.1.1", md5="cf210d4483b43fe95b2833f2608c1be0")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
