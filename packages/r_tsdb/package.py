# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsdb(RPackage):
	"""Terribly-Simple Data Base for Time Series

	A terribly-simple data base for numeric
  time series, written purely in R, so no external
  database-software is needed. Series are stored in
  plain-text files (the most-portable and enduring file
  type) in CSV format. Timestamps are encoded using R's
  native numeric representation for 'Date'/'POSIXct',
  which makes them fast to parse, but keeps them
  accessible with other software. The package provides
  tools for saving and updating series in this
  standardised format, for retrieving and joining data,
  for summarising files and directories, and for
  coercing series from and to other data types (such as
  'zoo' series).
	"""
	
	homepage = "http://enricoschumann.net/R/packages/tsdb/"
	cran = "tsdb" 

	version("1.1-0", md5="a8b345ebe499dd598da683f383f90302")

	depends_on("r-datetimeutils", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
