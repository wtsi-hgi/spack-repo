# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppclock(RPackage):
	"""Seamless 'Rcpp' Benchmarking

	Time the execution of overlapping or unique 'Rcpp' code chunks using convenient methods, seamlessly write timing results to an 'RcppClock' object in the R global environment, and summarize and/or plot the results in R.
	"""
	
	cran = "RcppClock" 

	version("1.1", md5="0fb9c16b60bc7629a7aa749eadd97cdd")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
