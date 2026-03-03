# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobustcalibration(RPackage):
	"""Robust Calibration of Imperfect Mathematical Models

	Implements full Bayesian analysis for calibrating mathematical models with new methodology for modeling the discrepancy function. It allows for emulation, calibration and prediction using complex mathematical model outputs and experimental data. See the reference: Mengyang Gu and Long Wang (2018) <arXiv:1707.08215>, Mengyang Gu, Fangzheng Xie and Long Wang (2021) <arXiv:1807.03829>, Mengyang Gu, Kyle Anderson and Erika McPhillips (2021) <arXiv:1810.11664>.
	"""
	
	cran = "RobustCalibration" 

	version("0.5.4", md5="59142631b6a26feb909a74969015a2d6")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-robustgasp@0.6.4:", type=("build", "run"))
	depends_on("r-nloptr@1.0.4:", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
