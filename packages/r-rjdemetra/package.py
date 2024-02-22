# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRjdemetra(RPackage):
	"""Interface to 'JDemetra+' Seasonal Adjustment Software

	Interface around 'JDemetra+' (<https://github.com/jdemetra/jdemetra-app>), the seasonal adjustment software officially
    recommended to the members of the European Statistical System (ESS) and the European System of Central Banks.
    It offers full access to all options and outputs of 'JDemetra+', including the two leading seasonal adjustment methods
    TRAMO/SEATS+ and X-12ARIMA/X-13ARIMA-SEATS.
	"""
	
	homepage = "https://jdemetra.github.io/rjdemetra/"
	cran = "RJDemetra" 

	version("0.2.5", md5="61dfc59703c78401b390866267e67f43")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-rjava@0.9.8:", type=("build", "run"))
	depends_on("openjdk@8:", type=("build", "link", "run"))
