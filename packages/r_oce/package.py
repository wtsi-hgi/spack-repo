# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROce(RPackage):
	"""Analysis of Oceanographic Data

	Supports the analysis of Oceanographic data, including 'ADCP'
    measurements, measurements made with 'argo' floats, 'CTD' measurements,
    sectional data, sea-level time series, coastline and topographic data, etc.
    Provides specialized functions for calculating seawater properties such as
    potential temperature in either the 'UNESCO' or 'TEOS-10' equation of state.
    Produces graphical displays that conform to the conventions of the
    Oceanographic literature. This package is discussed extensively by
    Kelley (2018) "Oceanographic Analysis with R" <doi:10.1007/978-1-4939-8844-0>.
	"""
	
	homepage = "https://dankelley.github.io/oce/"
	cran = "oce" 

	version("1.8-2", md5="19e0b2924454953cbe7aee9907a1f494")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-gsw", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
