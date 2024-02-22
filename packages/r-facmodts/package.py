# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFacmodts(RPackage):
	"""Time Series Factor Models for Asset Returns

	Supports teaching methods of estimating and testing time series
    factor models for use in robust portfolio construction and analysis. Unique
    in providing not only classical least squares, but also modern robust model
    fitting methods which are not much influenced by outliers. Includes
    returns and risk decompositions, with user choice of  standard deviation,
    value-at-risk, and expected shortfall risk measures. "Robust Statistics
    Theory and Methods (with R)", R. A. Maronna, R. D. Martin, V. J. Yohai, 
    M. Salibian-Barrera (2019) <doi:10.1002/9781119214656>.
	"""
	
	homepage = "https://github.com/robustport/facmodTS"
	cran = "facmodTS" 

	version("1.0", md5="daec9d3fa1c4be6f3e73323125c32144")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-lars", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-leaps", type=("build", "run"))
	depends_on("r-performanceanalytics", type=("build", "run"))
	depends_on("r-portfolioanalytics", type=("build", "run"))
	depends_on("r-r-cache", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-robstattm", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
