# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNonlinearicp(RPackage):
	"""Invariant Causal Prediction for Nonlinear Models

	Performs 'nonlinear Invariant Causal Prediction' to estimate the 
    causal parents of a given target variable from data collected in
    different experimental or environmental conditions, extending
    'Invariant Causal Prediction' from Peters, Buehlmann and Meinshausen (2016), 
    <arXiv:1501.01332>, to nonlinear settings. For more details, see C. Heinze-Deml, 
    J. Peters and N. Meinshausen: 'Invariant Causal Prediction for Nonlinear Models', 
    <arXiv:1706.08576>.
	"""
	
	homepage = "https://github.com/christinaheinze/nonlinearICP-and-CondIndTests"
	cran = "nonlinearICP" 

	version("0.1.2.1", md5="659c1705181d1f54394ab759f405771f")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-condindtests", type=("build", "run"))
	depends_on("r-data-tree", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
