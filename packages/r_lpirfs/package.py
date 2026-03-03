# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLpirfs(RPackage):
	"""Local Projections Impulse Response Functions

	Provides functions to estimate and visualize linear as well as nonlinear impulse 
             responses based on local projections by Jordà (2005) <doi:10.1257/0002828053828518>.
             The methods and the package are explained in detail in Adämmer (2019) <doi:10.32614/RJ-2019-052>.
	"""
	
	cran = "lpirfs" 

	version("0.2.3", md5="ce3cc59a98679c7805f1ba717f099cd8")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-doparallel@1.0.15:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-foreach@1.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-lmtest@0.9.36:", type=("build", "run"))
	depends_on("r-plm@2.2.3:", type=("build", "run"))
	depends_on("r-sandwich@2.5.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
