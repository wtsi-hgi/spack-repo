# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCodez(RPackage):
	"""Seq2Seq Encoder-Decoder Model for Time-Feature Analysis Based on
Tensorflow

	Proposes Seq2seq Time-Feature Analysis using an Encoder-Decoder to project into latent space and a Forward Network to predict the next sequence.
	"""
	
	homepage = "https://rpubs.com/giancarlo_vercellino/codez"
	cran = "codez" 

	version("1.0.0", md5="b5f13de21ef2f0fc365fcdd34a013134")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-abind@1.4.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.6:", type=("build", "run"))
	depends_on("r-readr@2.1.2:", type=("build", "run"))
	depends_on("r-fancova@0.6.1:", type=("build", "run"))
	depends_on("r-imputets@3.2:", type=("build", "run"))
	depends_on("r-modeest@2.4:", type=("build", "run"))
	depends_on("r-scales@1.1.1:", type=("build", "run"))
	depends_on("r-tictoc@1.0.1:", type=("build", "run"))
	depends_on("r-tensorflow@2.9:", type=("build", "run"))
	depends_on("r-keras@2.9:", type=("build", "run"))
	depends_on("r-moments@0.14:", type=("build", "run"))
	depends_on("r-narray@0.4.1.1:", type=("build", "run"))
	depends_on("r-fastdummies@1.6.3:", type=("build", "run"))
	depends_on("r-entropy@1.3.1:", type=("build", "run"))
	depends_on("r-philentropy@0.5:", type=("build", "run"))
	depends_on("r-greybox@1.0.1:", type=("build", "run"))
	depends_on("r-lubridate@1.7.10:", type=("build", "run"))
