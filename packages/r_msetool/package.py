# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsetool(RPackage):
	"""Management Strategy Evaluation Toolkit

	Development, simulation testing, and implementation of management procedures for fisheries 
    (see Carruthers & Hordyk (2018) <doi:10.1111/2041-210X.13081>).
	"""
	
	cran = "MSEtool" 

	version("3.7.1", md5="c85807f30f82cff3760265fcc3200d03")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-snowfall", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
