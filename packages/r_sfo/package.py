# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSfo(RPackage):
	"""San Francisco International Airport Monthly Air Passengers

	Provides monthly statistics on the number of monthly air passengers at SFO airport such as operating airline, terminal, geo, etc.
             Data source: San Francisco data portal (DataSF) <https://data.sfgov.org/Transportation/Air-Traffic-Passenger-Statistics/rkru-6vcg>.
	"""
	
	cran = "sfo" 

	version("0.1.2", md5="45fd8308f2968c131c3a344e652665c3")

	depends_on("r@2.10:", type=("build", "run"))
