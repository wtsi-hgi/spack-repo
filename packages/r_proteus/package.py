# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProteus(RPackage):
	"""Multiform Seq2Seq Model for Time-Feature Analysis

	Seq2seq time-feature analysis based on variational model, with a wide range of distributions available for the latent variable.
	"""
	
	homepage = "https://rpubs.com/giancarlo_vercellino/proteus"
	cran = "proteus" 

	version("1.1.4", md5="902d8a678cb02f0d83017413666dc1a5")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-abind@1.4.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.3:", type=("build", "run"))
	depends_on("r-ggthemes@4.2.4:", type=("build", "run"))
	depends_on("r-readr@1.4:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-lubridate@1.7.9.2:", type=("build", "run"))
	depends_on("r-narray@0.4.1:", type=("build", "run"))
	depends_on("r-fancova@0.6.1:", type=("build", "run"))
	depends_on("r-imputets@3.1:", type=("build", "run"))
	depends_on("r-modeest@2.4:", type=("build", "run"))
	depends_on("r-scales@1.1.1:", type=("build", "run"))
	depends_on("r-tictoc@1.0.1:", type=("build", "run"))
	depends_on("r-torch@0.3:", type=("build", "run"))
	depends_on("r-actuar@3.1.1:", type=("build", "run"))
	depends_on("r-vgam@1.1.5:", type=("build", "run"))
	depends_on("r-moments@0.14:", type=("build", "run"))
	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
	depends_on("r-greybox@1.0.7:", type=("build", "run"))
	depends_on("r-furrr@0.3.1:", type=("build", "run"))
	depends_on("r-future@1.33:", type=("build", "run"))
	depends_on("r-sn@2.1.1:", type=("build", "run"))
