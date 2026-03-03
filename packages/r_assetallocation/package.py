# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAssetallocation(RPackage):
	"""Backtesting Simple Asset Allocation Strategies

	Easy and quick testing of customizable asset allocation strategies.
    Users can rely on their own data, or have the package automatically
    download data from Yahoo Finance (<https://finance.yahoo.com/>). Several 
    pre-loaded portfolios with data are available, including some which are 
    discussed in Faber (2015, ISBN:9780988679924). 
	"""
	
	homepage = "https://github.com/rubetron/AssetAllocation"
	cran = "AssetAllocation" 

	version("1.1.1", md5="9d540912efb19fb4468609b4af3051c1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-performanceanalytics", type=("build", "run"))
	depends_on("r-quantmod", type=("build", "run"))
	depends_on("r-riskportfolios", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-nmof", type=("build", "run"))
	depends_on("r-riskparityportfolio", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
