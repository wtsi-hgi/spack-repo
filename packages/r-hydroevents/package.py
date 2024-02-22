# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHydroevents(RPackage):
	"""Extract Event Statistics in Hydrologic Time Series

	Events from individual hydrologic time series are extracted, and events from multiple time series can be matched to each other.
	Tang, W. & Carey, S. K. (2017) <doi:10.1002/hyp.11185>.
	Kaur, S., Horne, A., Stewardson, M.J., Nathan, R., Costa, A.M., Szemis, J.M., & Webb, J.A. (2017) <doi:10.1080/24705357.2016.1276418>.
	Ladson, A., Brown, R., Neal, B., & Nathan, R. J. (2013) <doi:10.7158/W12-028.2013.17.1>.
	"""
	
	homepage = "https://github.com/conradwasko/hydroEvents"
	cran = "hydroEvents" 

	version("0.11", md5="73e42fee1df5a1bb5af7e6d526c3fd18")

	depends_on("r@2.10:", type=("build", "run"))
