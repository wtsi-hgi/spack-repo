# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdp(RPackage):
	"""The Ramer-Douglas-Peucker Algorithm

	Pretty fast implementation of the Ramer-Douglas-Peucker algorithm for reducing the number of points on a 2D curve.
    Urs Ramer (1972), "An iterative procedure for the polygonal approximation of plane curves" <doi:10.1016/S0146-664X(72)80017-0>.
    David H. Douglas and Thomas K. Peucker (1973), "Algorithms for the Reduction of the Number of Points Required to Represent a Digitized Line or its Caricature" <doi:10.3138/FM57-6770-U75U-7727>.
	"""
	
	homepage = "https://github.com/robertdj/RDP"
	cran = "RDP" 

	version("0.3.0", md5="82484b51b438acd2885b35ef3afcb954")

	depends_on("r-rcpp", type=("build", "run"))
