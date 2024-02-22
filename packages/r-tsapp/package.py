# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsapp(RPackage):
	"""Time Series, Analysis and Application

	Accompanies the book Rainer Schlittgen and Cristina Sattarhoff (2020) <https://www.degruyter.com/view/title/575978>  "Angewandte Zeitreihenanalyse mit R, 4. Auflage" . The package contains the time series and functions used therein. It was developed over many years teaching courses about time series analysis.  
	"""
	
	cran = "tsapp" 

	version("1.0.4", md5="81b9b010fd4d48105c2ecca42c728b07")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-vars", type=("build", "run"))
	depends_on("r-fftwtools", type=("build", "run"))
	depends_on("r-hdm", type=("build", "run"))
	depends_on("fftw@3:", type=("build", "link", "run"))
