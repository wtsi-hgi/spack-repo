# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REadrm(RPackage):
	"""Fitting Dose-Response Models Using an Evolutionary Algorithm

	Fits dose-response models using an evolutionary
    algorithm to estimate the model parameters. The procedure currently
    can fit 3-parameter, 4-parameter, and 5-parameter log-logistic models
    as well as exponential models. Functions are also provided to plot,
    make predictions, and calculate confidence intervals for the resulting
    models. For details see "Nonlinear Dose-response Modeling of
    High-Throughput Screening Data Using an Evolutionary Algorithm",
    Ma, J., Bair, E., Motsinger-Reif, A.; Dose-Response
    18(2):1559325820926734 (2020) <doi:10.1177/1559325820926734>.
	"""
	
	cran = "eadrm" 

	version("0.1.4", md5="b53658eeb59292133cf10768b50d62b9")

	depends_on("r@2.10:", type=("build", "run"))
