# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTetragon(RPackage):
	"""Automatic Sequence Prediction by Expansion of the Distance
Matrix

	Each sequence is predicted by expanding the distance matrix. The compact set of hyper-parameters is tuned through random search.
	"""
	
	homepage = "https://rpubs.com/giancarlo_vercellino/tetragon"
	cran = "tetragon" 

	version("1.3.0", md5="618b164822b36f1a4e32c100048f262a")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-abind@1.4.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-readr@2.0.1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-lubridate@1.7.10:", type=("build", "run"))
	depends_on("r-narray@0.4.1.1:", type=("build", "run"))
	depends_on("r-imputets@3.2:", type=("build", "run"))
	depends_on("r-scales@1.1.1:", type=("build", "run"))
	depends_on("r-tictoc@1.0.1:", type=("build", "run"))
	depends_on("r-modeest@2.4:", type=("build", "run"))
	depends_on("r-moments@0.14:", type=("build", "run"))
	depends_on("r-greybox@1.0.1:", type=("build", "run"))
	depends_on("r-dqrng@0.3:", type=("build", "run"))
	depends_on("r-entropy@1.3.1:", type=("build", "run"))
	depends_on("r-rfast@2.0.6:", type=("build", "run"))
	depends_on("r-philentropy@0.5:", type=("build", "run"))
	depends_on("r-fastdummies@1.6.3:", type=("build", "run"))
	depends_on("r-fancova@0.6.1:", type=("build", "run"))
