# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNabor(RPackage):
	"""Wraps 'libnabo', a Fast K Nearest Neighbour Library for Low
Dimensions

	An R wrapper for 'libnabo', an exact or approximate k nearest
    neighbour library which is optimised for low dimensional spaces (e.g. 3D).
    'libnabo' has speed and space advantages over the 'ANN' library wrapped by
    package 'RANN'. 'nabor' includes a knn function that is designed as a 
    drop-in replacement for 'RANN' function nn2. In addition, objects which 
    include the k-d tree search structure can be returned to speed up repeated 
    queries of the same set of target points.
	"""
	
	homepage = "https://github.com/jefferis/nabor"
	cran = "nabor" 

	version("0.5.0", md5="edc94a57dbde3d51f532bcc324c4bac7")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.2.2:", type=("build", "run"))
	depends_on("r-bh@1.54.0.4:", type=("build", "run"))
