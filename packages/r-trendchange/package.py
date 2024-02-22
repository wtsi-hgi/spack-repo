# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrendchange(RPackage):
	"""Innovative Trend Analysis and Time-Series Change Point Analysis

	Innovative Trend Analysis is a graphical method to examine the trends in time series data. Sequential Mann-Kendall test uses the intersection of prograde and retrograde series to indicate the possible change point in time series data. Distribution free cumulative sum charts indicate location and significance of the change point in time series.
  Zekai, S. (2011). <doi:10.1061/(ASCE)HE.1943-5584.0000556>.
  Grayson, R. B. et al. (1996). Hydrological Recipes: Estimation Techniques in Australian Hydrology. Cooperative Research Centre for Catchment Hydrology, Australia, p. 125. 
  Sneyers, S. (1990). On the statistical analysis of series of observations. Technical note no 5 143, WMO No 725 415. Secretariat of the World Meteorological Organization, Geneva, 192 pp.
	"""
	
	cran = "trendchange" 

	version("1.2", md5="35da0e26c848ee941ca202a453b8a858")

	depends_on("r@2.10:", type=("build", "run"))
