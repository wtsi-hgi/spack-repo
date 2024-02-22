# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPowersdi(RPackage):
	"""Calculate Standardised Drought Indices Using NASA POWER Data

	A set of functions designed to calculate the standardised
    precipitation and standardised precipitation evapotranspiration indices
    using NASA POWER data as described in Blain et al. (2023)
    <doi:10.2139/ssrn.4442843>.  These indices are calculated using a reference
    data source.  The functions verify if the indices' estimates meet the
    assumption of normality and how well NASA POWER estimates represent
    real-world data.  Indices are calculated in a routine mode.  Potential
    evapotranspiration amounts and the difference between rainfall and potential
    evapotranspiration are also calculated.  The functions adopt a basic time
    scale that splits each month into four periods.  Days 1 to 7, days 8 to 14,
    days 15 to 21, and days 22 to 28, 29, 30, or 31, where 'TS=4' corresponds to
    a 1-month length moving window (calculated 4 times per month) and 'TS=48'
    corresponds to a 12-month length moving window (calculated 4 times per
    month).
	"""
	
	homepage = "https://github.com/gabrielblain/PowerSDI"
	cran = "PowerSDI" 

	version("1.0.0", md5="e545ef142b6c600025a6d3533d2d6a74")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-lmom", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-nasapower", type=("build", "run"))
