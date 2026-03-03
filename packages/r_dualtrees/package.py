# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDualtrees(RPackage):
	"""Decimated and Undecimated 2D Complex Dual-Tree Wavelet Transform

	An implementation of the decimated two-dimensional complex dual-tree wavelet transform as described in Kingsbury (1999) <doi:10.1098/rsta.1999.0447> and Selesnick et al. (2005) <doi:10.1109/MSP.2005.1550194>. Also includes the undecimated version and spectral bias correction described in Nelson et al. (2018) <doi:10.1007/s11222-017-9784-0>. The code is partly based on the 'dtcwt' Python library.
	"""
	
	cran = "dualtrees" 

	version("0.1.5", md5="064b729cf7d46257a16c7e34790ea866")

	depends_on("r@3.5:", type=("build", "run"))
