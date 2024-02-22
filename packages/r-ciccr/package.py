# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCiccr(RPackage):
	"""Causal Inference in Case-Control and Case-Population Studies

	Estimation and inference methods for causal relative and attributable risk in case-control and case-population studies
  under the monotone treatment response and monotone treatment selection assumptions.
  For more details, see the paper by Jun and Lee (2023), 
  "Causal Inference under Outcome-Based Sampling with Monotonicity Assumptions," <arXiv:2004.08318 [econ.EM]>,
  accepted for publication in Journal of Business & Economic Statistics.
	"""
	
	homepage = "https://github.com/sokbae/ciccr/"
	cran = "ciccr" 

	version("0.3.0", md5="2f16785ee2af26af16cafc3e13be0152")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
