# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuarks(RPackage):
	"""Simple Methods for Calculating and Backtesting Value at Risk and
Expected Shortfall

	Enables the user to calculate Value at Risk (VaR)
    and Expected Shortfall (ES) by means of various types of historical
    simulation. Currently plain-, age-, volatility-weighted- and filtered
    historical simulation are implemented in this package. Volatility weighting
    can be carried out via an exponentially weighted moving average model
    (EWMA) or other GARCH-type models. The performance can be assessed via
    Traffic Light Test, Coverage Tests and Loss Functions. The methods of the
    package are described in Gurrola-Perez, P. and Murphy, D. (2015)
    <https://EconPapers.repec.org/RePEc:boe:boeewp:0525> as well as McNeil, J.,
    Frey, R., and Embrechts, P. (2015) <https://ideas.repec.org/b/pup/pbooks/10496.html>.
	"""
	
	cran = "quarks" 

	version("1.1.3", md5="99788c970e8f7befe0af5afca79d3f5b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dygraphs", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rugarch", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-smoots", type=("build", "run"))
	depends_on("r-yfr", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
