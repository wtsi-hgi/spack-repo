# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBundesbank(RPackage):
	"""Download Data from Bundesbank

	Download data from the time-series
  databases of the Bundesbank, the German central
  bank. See the overview at the Bundesbank website
  (<https://www.bundesbank.de/en/statistics/time-series-databases>)
  for available series. The package provides only a
  single function, getSeries(), which supports both
  traditional and real-time datasets; it will also
  download meta data if available. Downloaded data
  can automatically be arranged in various formats,
  such as data frames or 'zoo' series. The data
  may optionally be cached, so as to avoid repeated
  downloads of the same series.
	"""
	
	homepage = "http://enricoschumann.net/R/packages/bundesbank/index.htm"
	cran = "bundesbank" 

	version("0.1-11", md5="196d728499e48ba8faaaa75e5e275b25")

