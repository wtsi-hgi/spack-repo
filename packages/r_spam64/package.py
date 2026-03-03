# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpam64(RPackage):
	"""64-Bit Extension of the SPArse Matrix R Package 'spam'

	Provides the Fortran code of the R package 'spam'
    with 64-bit integers. Loading this package together with the R package
    spam enables the sparse matrix class spam to handle huge sparse matrices
    with more than 2^31-1 non-zero elements.
    Documentation is provided in Gerber, Moesinger and Furrer (2017) <doi:10.1016/j.cageo.2016.11.015>.
	"""
	
	homepage = "https://git.math.uzh.ch/reinhard.furrer/spam"
	cran = "spam64" 

	version("2.10-0", md5="6ce179abd5a4bd34a9ea9b102a88ea74", url="https://cran.r-project.org/src/contrib/spam64_2.10-0.tar.gz")

