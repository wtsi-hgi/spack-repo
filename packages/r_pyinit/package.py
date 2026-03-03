# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPyinit(RPackage):
	"""Pena-Yohai Initial Estimator for Robust S-Regression

	Deterministic Pena-Yohai initial estimator for robust S estimators
    of regression. The procedure is described in detail in
    Pena, D., & Yohai, V. (1999) <doi:10.2307/2670164>.
	"""
	
	homepage = "https://github.com/dakep/pyinit"
	cran = "pyinit" 

	version("1.1.3", md5="555462777de66bfd8d938f23bd8479fa")

	depends_on("r-robustbase", type=("build", "run"))
