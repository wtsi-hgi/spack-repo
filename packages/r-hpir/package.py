# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHpir(RPackage):
	"""House Price Indexes

	Compute house price indexes and series using a variety of different methods and
    models common through the real estate literature.  Evaluate index 'goodness' based
    on accuracy, volatility and revision statistics. Background on basic model construction
    for repeat sales models can be found at: Case and Quigley (1991) 
    <https://ideas.repec.org/a/tpr/restat/v73y1991i1p50-58.html> and for hedonic pricing models at: 
    Bourassa et al (2006) <doi:10.1016/j.jhe.2006.03.001>. The package author's working paper on the 
    random forest approach to house price indexes can be found at: <http://www.github.com/andykrause/hpi_research>.
	"""
	
	homepage = "https://www.github.com/andykrause/hpiR"
	cran = "hpiR" 

	version("0.3.2", md5="092524c4f35ed769db5177caf96ceb82")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-imputets@3:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-pdp", type=("build", "run"))
