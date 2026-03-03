# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlicedlhd(RPackage):
	"""Sliced Latin Hypercube Designs

	A facility to generate sliced (orthogonal) Latin hypercube designs with four and five slices. For details about sliced and orthogonal Latin hypercube designs, see Yang, J. F., Lin, C. D., Qian, P. Z., and Lin, D. K. (2013). "Construction of sliced orthogonal Latin hypercube designs". Statistica Sinica, 1117-1130, <doi:10.5705/ss.2012.037>.
	"""
	
	cran = "SlicedLHD" 

	version("1.0", md5="c85caa3afbb6ed05927309ee7061a879")

	depends_on("r@4.3:", type=("build", "run"))
