# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQfratio(RPackage):
	"""Moments and Distributions of Ratios of Quadratic Forms Using
Recursion

	Evaluates moments of ratios (and products) of quadratic forms
    in normal variables, specifically using recursive algorithms developed by
    Bao and Kan (2013) <doi:10.1016/j.jmva.2013.03.002> and Hillier et al.
    (2014) <doi:10.1017/S0266466613000364>. Also provides distribution,
    quantile, and probability density functions of simple ratios of quadratic
    forms in normal variables with several algorithms. Originally developed as
    a supplement to Watanabe (2023) <doi:10.1007/s00285-023-01930-8> for
    evaluating average evolvability measures in evolutionary quantitative
    genetics, but can be used for a broader class of statistics. Generating 
    functions for these moments are also closely related to the top-order zonal
    and invariant polynomials of matrix arguments.
	"""
	
	homepage = "https://github.com/watanabe-j/qfratio"
	cran = "qfratio" 

	version("1.1.1", md5="1573fb573e3c40aed6fe91ab950f5b73")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
