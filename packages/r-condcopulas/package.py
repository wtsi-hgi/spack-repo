# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCondcopulas(RPackage):
	"""Estimation and Inference for Conditional Copula Models

	
    Provides functions for the estimation of conditional copulas models,
    various estimators of conditional Kendall's tau
    (proposed in Derumigny and Fermanian (2019a, 2019b, 2020)
    <doi:10.1515/demo-2019-0016>,
    <doi:10.1016/j.csda.2019.01.013>,
    <doi:10.1016/j.jmva.2020.104610>),
    and test procedures for the simplifying assumption
    (proposed in Derumigny and Fermanian (2017) <doi:10.1515/demo-2017-0011>
    and Derumigny, Fermanian and Min (2022) <doi:10.1002/cjs.11742>).
	"""
	
	homepage = "https://github.com/AlexisDerumigny/CondCopulas"
	cran = "CondCopulas" 

	version("0.1.3", md5="c0c471ad01dca5f5045504022663fccf")

	depends_on("r-vinecopula", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-ordinalnet", type=("build", "run"))
	depends_on("r-tree", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-data-tree", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-wdm", type=("build", "run"))
