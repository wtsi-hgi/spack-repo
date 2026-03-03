# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsbox(RPackage):
	"""Class-Agnostic Time Series

	Time series toolkit with identical behavior for all
  time series classes: 'ts','xts', 'data.frame', 'data.table', 'tibble', 'zoo',
  'timeSeries', 'tsibble', 'tis' or 'irts'. Also converts reliably between these classes.
	"""
	
	homepage = "https://docs.ropensci.org/tsbox/"
	cran = "tsbox" 

	version("0.4.1", md5="1ddbfc96bb76e8937eef8465c14a1199")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table@1.10:", type=("build", "run"))
	depends_on("r-anytime", type=("build", "run"))
