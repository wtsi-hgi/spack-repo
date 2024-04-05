# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlr3hyperband(RPackage):
	"""Hyperband for 'mlr3'

	Successive Halving (Jamieson and Talwalkar (2016)
    <arXiv:1502.07943>) and Hyperband (Li et al. 2018 <arXiv:1603.06560>)
    optimization algorithm for the mlr3 ecosystem. The implementation in
    mlr3hyperband features improved scheduling and parallelizes the evaluation
    of configurations. The package includes tuners for hyperparameter
    optimization in mlr3tuning and optimizers for black-box optimization in
    bbotk.
	"""
	
	homepage = "https://mlr3hyperband.mlr-org.com"
	cran = "mlr3hyperband" 

	version("0.5.0", md5="5c9dd2dcaece00718665d921430d192d")
	version("0.4.5", md5="ef4ca905aa2521c8285dac37856b4dc3")

	depends_on("r-mlr3tuning@0.13:", type=("build", "run"))
	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-bbotk@0.7:", type=("build", "run"))
	depends_on("r-checkmate@1.9.4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-lgr", type=("build", "run"))
	depends_on("r-mlr3@0.13.1:", type=("build", "run"))
	depends_on("r-mlr3misc@0.10:", type=("build", "run"))
	depends_on("r-paradox@0.9:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
