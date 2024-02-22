# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsemodr(RPackage):
	"""SPAtial Resolution-SEnsitive Models of Outbreak Dynamics

	Implementation of spatially-explicit, stochastic disease models with customizable time windows that describe how parameter values fluctuate during outbreaks (e.g., in response to public health or conservation interventions).
	"""
	
	homepage = "https://github.com/NAU-CCL/SPARSEMODr"
	cran = "SPARSEMODr" 

	version("1.2.0", md5="84a03099e9f842792c76787fe514d1cc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("gsl@2.7:", type=("build", "link", "run"))
