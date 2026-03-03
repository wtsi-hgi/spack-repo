# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REsback(RPackage):
	"""Expected Shortfall Backtesting

	Implementations of the expected shortfall backtests of Bayer and Dimitriadis (2020) <doi:10.1093/jjfinec/nbaa013> 
    as well as other well known backtests from the literature. Can be used to assess the correctness of forecasts of the 
    expected shortfall risk measure which is e.g. used in the banking and finance industry for quantifying the market risk 
    of investments. A special feature of the backtests of  Bayer and Dimitriadis (2020) <doi:10.1093/jjfinec/nbaa013> 
    is that they only require forecasts of  the expected shortfall, which is in striking contrast to all other existing 
    backtests, making them particularly attractive for practitioners.
	"""
	
	cran = "esback" 

	version("0.3.1", md5="4fcc6d63062e0e67b4af8c52bc0c8395")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-esreg", type=("build", "run"))
