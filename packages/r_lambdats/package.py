# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLambdats(RPackage):
	"""Variational Seq2Seq Model with Lambda Transformer for Time
Series Analysis

	Time series analysis based on lambda transformer and variational seq2seq, built on 'Torch'.
	"""
	
	cran = "lambdaTS" 

	version("1.1", md5="32538d4d97eba2267cf00b46e7d672b7")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-narray", type=("build", "run"))
	depends_on("r-fancova", type=("build", "run"))
	depends_on("r-imputets", type=("build", "run"))
	depends_on("r-modeest", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tictoc", type=("build", "run"))
	depends_on("r-bizdays", type=("build", "run"))
	depends_on("r-torch", type=("build", "run"))
