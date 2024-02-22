# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRctrep(RPackage):
	"""Validation of Estimates of Treatment Effects in Observational
Data

	Validates estimates of (conditional) average treatment effects obtained using observational data by a) making it easy to obtain and visualize estimates derived using a large variety of methods (G-computation, inverse propensity score weighting, etc.), and b) ensuring that estimates are easily compared to a gold standard (i.e., estimates derived from randomized controlled trials). 'RCTrep' offers a generic protocol for treatment effect validation based on four simple steps, namely, set-selection, estimation, diagnosis, and validation. 'RCTrep' provides a simple dashboard to review the obtained results. The validation approach is introduced by Shen, L., Geleijnse, G. and Kaptein, M. (2023) <doi:10.21203/rs.3.rs-2559287/v2>.
	"""
	
	homepage = "https://github.com/duolajiang/RCTrep"
	cran = "RCTrep" 

	version("1.2.0", md5="1bbb8bc87f32e2be33b308b8a7a20502")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-matchit", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-psweight", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-geex", type=("build", "run"))
	depends_on("r-bart", type=("build", "run"))
	depends_on("r-fastdummies", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
