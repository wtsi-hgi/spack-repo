# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMdei(RPackage):
	"""Implementing the Method of Direct Estimation and Inference

	Causal and statistical inference on an arbitrary treatment
    effect curve requires care in both estimation and inference.  This
    package, implements the Method of Direct Estimation and Inference as introduced in "Estimation and Inference on Nonlinear and Heterogeneous Effects" by Ratkovic and Tingley (2023) <doi:10.1086/723811>.  The method takes an outcome, variable of theoretical interest
    (treatment), and set of variables and then returns a partial
    derivative (marginal effect) of the treatment variable at each point
    along with uncertainty intervals. The approach offers two advances.
    First, a split-sample approach is used as a guard against over-fitting.
    Second, the method uses a data-driven interval derived from conformal
    inference, rather than relying on a normality assumption on the error
    terms.
	"""
	
	cran = "MDEI" 

	version("1.0", md5="4ab5659b74c0385f477bc5ccfcb7957d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-splines2", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
