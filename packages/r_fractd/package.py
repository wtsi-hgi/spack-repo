# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFractd(RPackage):
	"""Estimation of Fractal Dimension of a Black Area in 2D and 3D
(Slices) Images

	Estimate the of fractal dimension of a black area in 2D and 3D (slices) images using the box-counting method. See Klinkenberg B. (1994) <doi:10.1007/BF02065874>.
	"""
	
	cran = "fractD" 

	version("0.1.0", md5="2e4aec75cf0902f575a859fc6330c046")

	depends_on("r-imager@0.42.1:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
