# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSslasso(RPackage):
	"""The Spike-and-Slab LASSO

	Efficient coordinate ascent algorithm for fitting regularization paths for linear models penalized by Spike-and-Slab LASSO of Rockova and George (2018) <doi:10.1080/01621459.2016.1260469>.
	"""
	
	homepage = "http://faculty.chicagobooth.edu/veronika.rockova/ssl.pdf"
	cran = "SSLASSO" 

	version("1.2-2", md5="d0d864713c2976b39b529c2ed1cf92db")

