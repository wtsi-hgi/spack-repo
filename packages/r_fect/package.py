# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFect(RPackage):
	"""Fixed Effects Counterfactuals

	Estimates causal effects with panel data using the counterfactual methods. It is suitable for panel or time-series cross-sectional analysis with binary treatments under (hypothetically) baseline randomization.It allows a treatment to switch on and off and limited carryover effects. It supports linear factor models, a generalization of gsynth and the matrix completion method. Implementation details can be found in Liu, Wang and Xu (2022) <arXiv:2107.00856>.
	"""
	
	homepage = "https://yiqingxu.org/packages/fect/articles/tutorial.html"
	cran = "fect" 

	version("1.0.0", md5="730c36e2529f4eac5b86182c662221f6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-ggally@1.0.1:", type=("build", "run"))
	depends_on("r-doparallel@1.0.10:", type=("build", "run"))
	depends_on("r-foreach@1.4.3:", type=("build", "run"))
	depends_on("r-abind@1.4.0:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-fixest", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-panelview", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
