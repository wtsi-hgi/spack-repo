# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowscreen(RPackage):
	"""Daily Streamflow Trend and Change Point Screening

	Screens daily streamflow time series for temporal trends and
    change-points. This package has been primarily developed for assessing the
    quality of daily streamflow time series. It also contains tools for plotting
    and calculating many different streamflow metrics. The package can be used to
    produce summary screening plots showing change-points and significant temporal
    trends for high flow, low flow, and/or baseflow statistics, or it can be used
    to perform more detailed hydrological time series analyses. The package was
    designed for screening daily streamflow time series from Water Survey Canada
    and the United States Geological Survey but will also work with streamflow time
    series from many other agencies.
	"""
	
	cran = "FlowScreen" 

	version("1.2.6", md5="39fca2ddf02463c112d64344da98e0c3")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-zyp", type=("build", "run"))
	depends_on("r-changepoint", type=("build", "run"))
	depends_on("r-evir", type=("build", "run"))
