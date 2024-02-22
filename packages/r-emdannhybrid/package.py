# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmdannhybrid(RPackage):
	"""Empirical Mode Decomposition Based Artificial Neural Network
Model

	Application of empirical mode decomposition based artificial neural network model for nonlinear and non stationary univariate time series forecasting. For method details see (i) Choudhury (2019) <https://www.indianjournals.com/ijor.aspx?target=ijor:ijee3&volume=55&issue=1&article=013>; (ii) Das (2020) <https://www.indianjournals.com/ijor.aspx?target=ijor:ijee3&volume=56&issue=2&article=002>.
	"""
	
	cran = "EMDANNhybrid" 

	version("0.2.0", md5="557f4ba57dd2818e799068c361d9dc37")

	depends_on("r-emd", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
