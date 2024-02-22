# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcompanion(RPackage):
	"""Objects and Methods for Multi-Companion Matrices

	
    Provides a class for multi-companion matrices with methods for
    arithmetic and factorization.  A method for generation of
    multi-companion matrices with prespecified spectral properties is
    provided, as well as some utilities for periodically correlated and
    multivariate time series models. See Boshnakov (2002)
    <doi:10.1016/S0024-3795(01)00475-X> and Boshnakov & Iqelan (2009)
    <doi:10.1111/j.1467-9892.2009.00617.x>.
	"""
	
	homepage = "https://geobosh.github.io/mcompanion/"
	cran = "mcompanion" 

	version("0.6", md5="b674c70585a6cbc91d6d2fda43dc39ea")

	depends_on("r-matrix@1.5.0:", type=("build", "run"))
	depends_on("r-gbutils", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
