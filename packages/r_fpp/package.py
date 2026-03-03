# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFpp(RPackage):
	"""Data for "Forecasting: principles and practice"

	All data sets required for the examples and exercises in
        the book "Forecasting: principles and practice" by Rob J
        Hyndman and George Athanasopoulos. All packages required to run
        the examples are also loaded.
	"""
	
	homepage = "http://otexts.com/fpp/"
	cran = "fpp" 

	version("0.5", md5="297b90fba25486f07c211ff714cfb6e9")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-fma", type=("build", "run"))
	depends_on("r-expsmooth", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
