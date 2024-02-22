# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrtmle(RPackage):
	"""Doubly-Robust Nonparametric Estimation and Inference

	Targeted minimum loss-based estimators of counterfactual means and
    causal effects that are doubly-robust with respect both to consistency and
    asymptotic normality (Benkeser et al (2017), <doi:10.1093/biomet/asx053>; MJ
    van der Laan (2014), <doi:10.1515/ijb-2012-0038>).
	"""
	
	homepage = "https://github.com/benkeser/drtmle"
	cran = "drtmle" 

	version("1.1.2", md5="db7213faf3face7429db9b297549a1a4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-superlearner", type=("build", "run"))
	depends_on("r-np", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
