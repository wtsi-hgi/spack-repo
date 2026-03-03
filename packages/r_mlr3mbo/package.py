# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlr3mbo(RPackage):
	"""Flexible Bayesian Optimization

	A modern and flexible approach to Bayesian Optimization / Model
    Based Optimization building on the 'bbotk' package. 'mlr3mbo' is a toolbox
    providing both ready-to-use optimization algorithms as well as their fundamental
    building blocks allowing for straightforward implementation of custom
    algorithms. Single- and multi-objective optimization is supported as well as
    mixed continuous, categorical and conditional search spaces. Moreover, using
    'mlr3mbo' for hyperparameter optimization of machine learning models within the
    'mlr3' ecosystem is straightforward via 'mlr3tuning'. Examples of ready-to-use
    optimization algorithms include Efficient Global Optimization by Jones et al.
    (1998) <doi:10.1023/A:1008306431147>, ParEGO by Knowles (2006)
    <doi:10.1109/TEVC.2005.851274> and SMS-EGO by Ponweiser et al. (2008)
    <doi:10.1007/978-3-540-87700-4_78>.
	"""
	
	homepage = "https://mlr3mbo.mlr-org.com"
	cran = "mlr3mbo" 

	version("0.2.2", md5="3c245f209295566327d2c2b7588ac8aa")
	version("0.2.1", md5="f1ababcbd9890756374bf8195205c580")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-bbotk@0.5.4:", type=("build", "run"))
	depends_on("r-checkmate@2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-lgr@0.3.4:", type=("build", "run"))
	depends_on("r-mlr3@0.14:", type=("build", "run"))
	depends_on("r-mlr3misc@0.11:", type=("build", "run"))
	depends_on("r-mlr3tuning@0.14:", type=("build", "run"))
	depends_on("r-paradox@0.10:", type=("build", "run"))
	depends_on("r-spacefillr", type=("build", "run"))
	depends_on("r-r6@2.4.1:", type=("build", "run"))
