# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFacmodcs(RPackage):
	"""Cross-Section Factor Models

	Linear cross-section factor model fitting with least-squares 
    and robust fitting the 'lmrobdetMM()' function from 'RobStatTM'; related
    volatility, Value at Risk and Expected Shortfall risk and performance 
    attribution (factor-contributed vs idiosyncratic returns);
    tabular displays of risk and performance reports;
    factor model Monte Carlo. The package authors would like to thank Chicago
    Research on Security Prices,LLC for the cross-section of about 300
    CRSP stocks data (in the data.table object 'stocksCRSP', and S&P GLOBAL MARKET
    INTELLIGENCE for contributing 14 factor scores (a.k.a "alpha factors".and
    "factor exposures") fundamental data on the 300 companies in the data.table
    object 'factorSPGMI'.  The 'stocksCRSP' and 'factorsSPGMI' data are not covered by
    the GPL-2 license, are not provided as open source of any kind, and they are
    not to be redistributed in any form.
	"""
	
	homepage = "https://github.com/robustport/facmodCS"
	cran = "facmodCS" 

	version("1.0", md5="7a1204bf2a79cda5efdf585aadf431ff")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-performanceanalytics", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-robstattm", type=("build", "run"))
