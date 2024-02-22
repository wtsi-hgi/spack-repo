# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImageLinesegmentdetector(RPackage):
	"""Detect Line Segments in Images

	An implementation of the Line Segment Detector on digital images described in the paper: "LSD: A Fast Line Segment Detector with a False Detection Control" by Rafael Grompone von Gioi et al (2012). 
    The algorithm is explained at <doi:10.5201/ipol.2012.gjmr-lsd>.
	"""
	
	homepage = "https://github.com/bnosac/image"
	cran = "image.LineSegmentDetector" 

	version("0.1.0", md5="025676a9403730c420b1becee1c494b7")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
