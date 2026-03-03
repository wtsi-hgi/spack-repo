# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPmwr(RPackage):
	"""Portfolio Management with R

	Functions and examples for 'Portfolio Management
  with R': backtesting investment and trading strategies,
  computing profit/loss and returns, analysing trades,
  handling lists of transactions, reporting, and more.
	"""
	
	homepage = "http://enricoschumann.net/PMwR/"
	cran = "PMwR" 

	version("0.19-3", md5="b8bcc23d2a27635bdf557d3122b37498")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-nmof", type=("build", "run"))
	depends_on("r-datetimeutils", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
	depends_on("r-orgutils", type=("build", "run"))
	depends_on("r-textutils", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
