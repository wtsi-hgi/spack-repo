# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMtaft(RPackage):
	"""Data-Driven Estimation for Multi-Threshold Accelerate Failure
Time Model

	Developed a data-driven estimation framework for the multi-threshold accelerate failure time (MTAFT) model. The MTAFT model features different linear forms in different subdomains, and one of the major challenges is determining the number of threshold effects. The package introduces a data-driven approach that utilizes a Schwarz' information criterion, which demonstrates consistency under mild conditions. Additionally, a cross-validation (CV) criterion with an order-preserved sample-splitting scheme is proposed to achieve consistent estimation, without the need for additional parameters. The package establishes the asymptotic properties of the parameter estimates and includes an efficient score-type test to examine the existence of threshold effects. The methodologies are supported by numerical experiments and theoretical results, showcasing their reliable performance in finite-sample cases.
	"""
	
	cran = "MTAFT" 

	version("0.1.0", md5="f2a38d030e8be2e22ae11809f1ca750f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-grpreg", type=("build", "run"))
