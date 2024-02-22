# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSensobol(RPackage):
	"""Computation of Variance-Based Sensitivity Indices

	It allows to rapidly compute, bootstrap and plot up to fourth-order Sobol'-based sensitivity indices using several state-of-the-art first and total-order estimators. Sobol' indices can be computed either for models that yield a scalar as a model output or for systems of differential equations. The package also provides a suit of benchmark tests functions and several options to obtain publication-ready figures of the model output uncertainty and sensitivity-related analysis. An overview of the package can be found in Puy et al. (2022) <doi:10.18637/jss.v102.i05>. 
	"""
	
	homepage = "https://github.com/arnaldpuy/sensobol"
	cran = "sensobol" 

	version("1.1.5", md5="2b38cba8938aa9afbd2e254bf9a23446")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-boot@1.3.20:", type=("build", "run"))
	depends_on("r-data-table@1.12:", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-lhs@1.0.2:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-matrixstats@0.54:", type=("build", "run"))
	depends_on("r-randtoolbox@1.17.1:", type=("build", "run"))
	depends_on("r-desolve@1.27.1:", type=("build", "run"))
	depends_on("r-rdpack@2.1.2:", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-rlang@0.3.1:", type=("build", "run"))
	depends_on("r-scales@1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
