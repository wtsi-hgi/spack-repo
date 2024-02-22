# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRemoteparts(RPackage):
	"""Spatiotemporal Autoregression Analyses for Large Data Sets

	
  These tools were created to test map-scale hypotheses about trends in large
  remotely sensed data sets but any data with spatial and temporal variation
  can be analyzed. Tests are conducted using the PARTS method for analyzing spatially
  autocorrelated time series
  (Ives et al., 2021: <doi:10.1016/j.rse.2021.112678>).
  The method's unique approach can handle extremely large data sets that other
  spatiotemporal models cannot, while still appropriately accounting for
  spatial and temporal autocorrelation. This is done by partitioning the data
  into smaller chunks, analyzing chunks separately and then combining the
  separate analyses into a single, correlated test of the map-scale hypotheses.
	"""
	
	homepage = "https://github.com/morrowcj/remotePARTS"
	cran = "remotePARTS" 

	version("1.0.4", md5="87e00497d5aeca5ae2de2045d4b2d1c3")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-geosphere@1.5.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
