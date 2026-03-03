# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REchoice2(RPackage):
	"""Choice Models with Economic Foundation

	Implements choice models based on economic theory, including estimation using Markov chain Monte Carlo (MCMC), prediction, and more. Its usability is inspired by ideas from 'tidyverse'. Models include versions of the Hierarchical Multinomial Logit and Multiple Discrete-Continous (Volumetric) models with and without screening. The foundations of these models are described in Allenby, Hardt and Rossi (2019)  <doi:10.1016/bs.hem.2019.04.002>. Models with conjunctive screening are described in Kim, Hardt, Kim and Allenby (2022) <doi:10.1016/j.ijresmar.2022.04.001>. Models with set-size variation are described in Hardt and Kurz (2020) <doi:10.2139/ssrn.3418383>.
	"""
	
	homepage = "https://github.com/ninohardt/echoice2"
	cran = "echoice2" 

	version("0.2.4", md5="2eafb9d7fabc3d593b42c9a546fdb7c9", url="https://cran.r-project.org/src/contrib/echoice2_0.2.4.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
