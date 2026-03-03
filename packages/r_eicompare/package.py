# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REicompare(RPackage):
	"""Compares Different Ecological Inference Methods

	Provides a comprehensive suite of tools for estimating the candidate preferences of racial/ethnic voting blocs in elections. Includes functions for predicting voter race/ethnicity and conducting ecological inference. Race/ethnicity prediction builds on race prediction developed by Imai et al. (2016) <doi:10.1093/pan/mpw001>. Ecological inference methods are based on King (1997) <ISBN: 0691012407>, <https://gking.harvard.edu/eicamera/kinroot.html>; King et. al. (2004) <ISBN: 0521542804>, <https://gking.harvard.edu/files/abs/ecinf04-abs.shtml>.
	"""
	
	homepage = "https://github.com/RPVote/eiCompare"
	cran = "eiCompare" 

	version("3.0.4", md5="90dcc3ce3449dcfde036e588bd352128")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-eipack", type=("build", "run"))
	depends_on("r-ei", type=("build", "run"))
	depends_on("r-wru@1:", type=("build", "run"))
	depends_on("r-bayestestr", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mcmcse", type=("build", "run"))
	depends_on("r-overlapping", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
