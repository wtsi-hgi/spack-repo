# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppbdt(RPackage):
	"""'Rcpp' Bindings for the Boost Date_Time Library

	Access to Boost Date_Time functionality for dates,
 durations (both for days and date time objects), time zones, and 
 posix time ('ptime') is provided by using 'Rcpp modules'. The 
 posix time implementation can support high-resolution of up to 
 nano-second  precision by using 96 bits (instead of R's 64)
 to present a 'ptime' object (but this needs recompilation with
 a #define set).
	"""
	
	homepage = "https://github.com/eddelbuettel/rcppbdt"
	cran = "RcppBDT" 

	version("0.2.6", md5="4c1e124c6132b877a946cd7f9ae1b75f")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
