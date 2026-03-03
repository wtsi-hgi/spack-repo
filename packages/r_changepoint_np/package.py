# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChangepointNp(RPackage):
	"""Methods for Nonparametric Changepoint Detection

	Implements the multiple changepoint algorithm PELT with a nonparametric cost function based on the empirical distribution of the data. This package extends the changepoint package (see Killick, R and Eckley, I (2014) <doi:10.18637/jss.v058.i03> ).
	"""
	
	cran = "changepoint.np" 

	version("1.0.5", md5="f5d7e5bc1fb1add7ba96e38051d2a333")

	depends_on("r-changepoint", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
