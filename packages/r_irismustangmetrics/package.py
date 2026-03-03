# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIrismustangmetrics(RPackage):
	"""Statistics and Metrics for Seismic Data

	Classes and functions for metrics calculation as part of the
             'IRIS DMC MUSTANG' project. The functionality in this package 
             builds upon the base classes of the 'IRISSeismic' package.
             Metrics include basic statistics as well as higher level
             'health' metrics that can help identify problematic seismometers.
	"""
	
	cran = "IRISMustangMetrics" 

	version("2.4.6", md5="56b3b21deb51704b002a0ec20b2507f8")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-irisseismic@1.3:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-seismicroll@1.1.4:", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-dplyr@0.4.3:", type=("build", "run"))
