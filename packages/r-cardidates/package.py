# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCardidates(RPackage):
	"""Identification of Cardinal Dates in Ecological Time Series

	Identification of cardinal dates
             (begin, time of maximum, end of mass developments)
             in ecological time series using fitted Weibull functions.
	"""
	
	homepage = "http://cardidates.r-forge.r-project.org"
	cran = "cardidates" 

	version("0.4.9", md5="a54acc554c93352899de508f0d856d2a")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-pastecs", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
