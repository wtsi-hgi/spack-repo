# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMerderiv(RPackage):
	"""Case-Wise and Cluster-Wise Derivatives for Mixed Effects Models

	Compute case-wise and cluster-wise derivative for mixed effects models with respect to fixed effects parameter, random effect (co)variances, and residual variance. This material is partially based on work supported by the National Science Foundation under Grant Number 1460719.
	"""
	
	homepage = "https://github.com/nctingwang/merDeriv"
	cran = "merDeriv" 

	version("0.2-4", md5="4161504372d83be98271731056c28817")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-lme4@1.1.10:", type=("build", "run"))
	depends_on("r-nonnest2", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
