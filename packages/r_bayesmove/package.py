# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesmove(RPackage):
	"""Non-Parametric Bayesian Analyses of Animal Movement

	Methods for assessing animal movement from telemetry and biologging
    data using non-parametric Bayesian methods. This includes features for pre-
    processing and analysis of data, as well as the visualization of results
    from the models. This framework does not rely on standard parametric density
    functions, which provides flexibility during model fitting. Further details 
    regarding part of this framework can be found in Cullen et al. (2021) <doi:10.1101/2020.11.05.369702>.
	"""
	
	homepage = "https://github.com/joshcullen/bayesmove"
	cran = "bayesmove" 

	version("0.2.1", md5="2da96f60a4be258b02fe15f98e117466")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-furrr@0.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
	depends_on("r-mcmcpack@1.4.5:", type=("build", "run"))
	depends_on("r-progress@1.2.2:", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tictoc@1:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-future@1.15.1:", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-dygraphs@1.1:", type=("build", "run"))
	depends_on("r-leaflet@2:", type=("build", "run"))
	depends_on("r-sf@0.9.6:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
