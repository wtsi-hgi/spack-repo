# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtfa(RPackage):
	"""Robust Factor Analysis for Tensor Time Series

	Tensor Factor Models (TFM) are appealing dimension reduction tools for high-order tensor time series, and have wide applications in economics, finance and medical imaging. We propose an one-step projection estimator by minimizing the least-square loss function, and further propose a robust estimator with an iterative weighted projection technique by utilizing the Huber loss function. The methods are discussed in Barigozzi et al. (2022) <arXiv:2206.09800>, and Barigozzi et al. (2023) <arXiv:2303.18163>.
	"""
	
	cran = "RTFA" 

	version("0.1.0", md5="00f02b71506bc0bb748a68bd798d8cce")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rtensor", type=("build", "run"))
	depends_on("r-tensor", type=("build", "run"))
