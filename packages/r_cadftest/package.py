# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCadftest(RPackage):
	"""A Package to Perform Covariate Augmented Dickey-Fuller Unit Root
Tests

	Hansen's (1995) Covariate-Augmented
        Dickey-Fuller (CADF) test. The only required argument is y, the
        Tx1 time series to be tested. If no stationary covariate X is
        passed to the procedure, then an ordinary ADF test is
        performed. The p-values of the test are computed using the
        procedure illustrated in Lupi (2009).
	"""
	
	homepage = "http://www.jstatsoft.org/v32/i02"
	cran = "CADFtest" 

	version("0.3-3", md5="e29f616625587da73de7d48d3add2a89")

	depends_on("r-dynlm", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-urca", type=("build", "run"))
