# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCondindtests(RPackage):
	"""Nonlinear Conditional Independence Tests

	Code for a variety of nonlinear conditional independence tests: 
  Kernel conditional independence test (Zhang et al., UAI 2011, <arXiv:1202.3775>),
  Residual Prediction test (based on Shah and Buehlmann, <arXiv:1511.03334>),
  Invariant environment prediction,
  Invariant target prediction,
  Invariant residual distribution test,
  Invariant conditional quantile prediction (all from Heinze-Deml et al., <arXiv:1706.08576>).
	"""
	
	homepage = "https://github.com/christinaheinze/nonlinearICP-and-CondIndTests"
	cran = "CondIndTests" 

	version("0.1.5", md5="dd6499a5db58067bf3189bf0bb1334d7")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-quantregforest", type=("build", "run"))
	depends_on("r-lawstat", type=("build", "run"))
	depends_on("r-rptests", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-mize", type=("build", "run"))
