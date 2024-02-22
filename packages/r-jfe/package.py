# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJfe(RPackage):
	"""Tools for Analyzing Time Series Data of Just Finance and
Econometrics

	Offers procedures to support financial and economic time series modelling and enhanced procedures for computing the investment performance indices of Bacon (2004) <DOI:10.1002/9781119206309>.
	"""
	
	cran = "JFE" 

	version("2.5.6", md5="b9dacf4366d591bb7aff889f768fab69")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
