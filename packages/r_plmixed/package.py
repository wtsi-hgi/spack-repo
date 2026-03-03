# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlmixed(RPackage):
	"""Estimate (Generalized) Linear Mixed Models with Factor
Structures

	Utilizes the 'lme4' and 'optimx' packages (previously the optim()
    function from 'stats') to estimate (generalized) linear mixed models (GLMM)
    with factor structures using a profile likelihood approach, as outlined in
    Jeon and Rabe-Hesketh (2012) <doi:10.3102/1076998611417628> and
    Rockwood and Jeon (2019) <doi:10.1080/00273171.2018.1516541>.
    Factor analysis and item response models can be extended to allow
    for an arbitrary number of nested and crossed random effects,
    making it useful for multilevel and cross-classified models.
	"""
	
	cran = "PLmixed" 

	version("0.1.7", md5="3357c712155db9d5a0a06e1e341a8f00")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-matrix@1.1.1:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
