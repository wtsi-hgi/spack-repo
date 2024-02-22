# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJubilee(RPackage):
	"""Forecasting Long-Term Growth of the U.S. Stock Market and
Business Cycles

	A long-term forecast model called "Jubilee-Tectonic model" is implemented to forecast future returns of the U.S. stock market, Treasury yield, and gold price. The five-factor model forecasts the 10-year and 20-year future equity returns with high R-squared above 80 percent. It is based on linear growth and mean reversion characteristics in the U.S. stock market. This model also enhances the CAPE model by introducing the hypothesis that there are fault lines in the historical CAPE, which can be calibrated and corrected through statistical learning. In addition, it contains a module for business cycles, optimal interest rate, and recession forecasts.
	"""
	
	homepage = "https://ssrn.com/abstract=3156574"
	cran = "jubilee" 

	version("0.3.3", md5="7e350b76b87397ecc0dd185294124234")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-readxl@1.3.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
