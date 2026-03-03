# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMiwqs(RPackage):
	"""Multiple Imputation Using Weighted Quantile Sum Regression

	The miWQS package handles the uncertainty due to below the detection limit in a correlated component mixture problem.  Researchers want to determine if a set/mixture of continuous and correlated components/chemicals is associated with an outcome and if so, which components are important in that mixture. These components share a common outcome but are interval-censored between zero and low thresholds, or detection limits, that may be different across the components. This package applies the multiple imputation (MI) procedure to the weighted quantile sum regression (WQS) methodology for continuous, binary, or count outcomes (Hargarten & Wheeler (2020) <doi:10.1016/j.envres.2020.109466>). The imputation models are: bootstrapping imputation (Lubin et.al (2004) <doi:10.1289/ehp.7199>), univariate Bayesian imputation (Hargarten & Wheeler (2020) <doi:10.1016/j.envres.2020.109466>), and multivariate Bayesian regression imputation.  
	"""
	
	cran = "miWQS" 

	version("0.4.4", md5="8860bd89943ee743e25a047f20352f43")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-coda@0.19.2:", type=("build", "run"))
	depends_on("r-condmvnorm@2015.2.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-glm2@1.2.1:", type=("build", "run"))
	depends_on("r-hmisc@4.1.1:", type=("build", "run"))
	depends_on("r-invgamma@1.1:", type=("build", "run"))
	depends_on("r-mass@7.3.49:", type=("build", "run"))
	depends_on("r-matrixnormal@0:", type=("build", "run"))
	depends_on("r-mcmcpack@1.4.4:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.10:", type=("build", "run"))
	depends_on("r-purrr@0.3.2:", type=("build", "run"))
	depends_on("r-rlist@0.4.6.1:", type=("build", "run"))
	depends_on("r-rsolnp@1.16:", type=("build", "run"))
	depends_on("r-survival@3.1.12:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-tmvmixnorm@1.0.2:", type=("build", "run"))
	depends_on("r-tmvtnorm@1.4.10:", type=("build", "run"))
	depends_on("r-truncnorm@1.0.8:", type=("build", "run"))
