# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQlcal(RPackage):
	"""R Bindings to the Calendaring Functionality of 'QuantLib'

	'QuantLib' bindings are provided for R using 'Rcpp' via an evolved version
 of the initial header-only 'Quantuccia' project offering an subset of 'QuantLib' (now
 maintained separately just for the calendaring subset). See the included file 'AUTHORS'
 for a full list of contributors to 'QuantLib' (and hence also 'Quantuccia').
	"""
	
	homepage = "https://github.com/qlcal/qlcal-r"
	cran = "qlcal" 

	version("0.0.10", md5="67f7e4db4777235cda5c646f2e49ad59")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
