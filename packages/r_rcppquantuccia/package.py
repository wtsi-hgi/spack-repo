# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppquantuccia(RPackage):
	"""R Bindings to the Calendaring Functionality of 'QuantLib'

	'QuantLib' bindings are provided for R using 'Rcpp' via an updated
 variant of the header-only 'Quantuccia' project (put together initially by Peter
 Caspers) offering an essential subset of 'QuantLib' (and now maintained separately
 for the calendaring subset). See the included file 'AUTHORS' for a full list of
 contributors to both 'QuantLib' and 'Quantuccia'.
	"""
	
	homepage = "https://github.com/eddelbuettel/rcppquantuccia"
	cran = "RcppQuantuccia" 

	version("0.1.2", md5="624cffc8a2f949e899d89f6814a1480b")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
