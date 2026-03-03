# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMfilter(RPackage):
	"""Miscellaneous Time Series Filters

	The mFilter package implements several time series filters useful
        for smoothing and extracting trend and cyclical components of a
        time series. The routines are commonly used in economics and
        finance, however they should also be interest to other areas.
        Currently, Christiano-Fitzgerald, Baxter-King,
        Hodrick-Prescott, Butterworth, and trigonometric regression
        filters are included in the package.
	"""
	
	homepage = "http://www.mbalcilar.net"
	cran = "mFilter" 

	version("0.1-5", md5="b3914f75d99f6825ce645253e831bbb2")

	depends_on("r@2.2:", type=("build", "run"))
