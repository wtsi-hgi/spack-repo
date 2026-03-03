# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirtcat(RPackage):
	"""Computerized Adaptive Testing with Multidimensional Item
Response Theory

	Provides tools to generate HTML interfaces for adaptive
    and non-adaptive tests using the shiny
    package (Chalmers (2016) <doi:10.18637/jss.v071.i05>). 
    Suitable for applying unidimensional and multidimensional
    computerized adaptive tests (CAT) using item response theory methodology and for
    creating simple questionnaires forms to collect response data directly in R.
    Additionally, optimal test designs (e.g., "shadow testing") are supported
    for tests that contain a large number of item selection constraints.
    Finally, package contains tools useful for performing Monte Carlo simulations 
    for studying test item banks.
	"""
	
	homepage = "https://github.com/philchalmers/mirtCAT"
	cran = "mirtCAT" 

	version("1.13", md5="073c26bac8cfd07293781839f556296e")

	depends_on("r-mirt@1.37:", type=("build", "run"))
	depends_on("r-shiny@1.0.1:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
