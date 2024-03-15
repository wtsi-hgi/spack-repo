# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSinrelefLd(RPackage):
	"""Reliability and Relative Efficiency in Locally-Dependent
Measures

	Implements an approach aimed at assessing the accuracy and
    effectiveness of raw scores obtained in scales that contain locally dependent
    items. The program uses as input the calibration (structural) item estimates
    obtained from fitting extended unidimensional factor-analytic solutions in
    which the existing local dependencies are included. Measures of reliability
    (Omega) and information are proposed at three levels: (a) total score, (b)
    bivariate-doublet, and (c) item-by-item deletion, and  are compared to those
    that would be obtained if all the items had been locally independent. All the
    implemented procedures can be obtained from: (a) linear factor-analytic
    solutions in which the item scores are treated as approximately continuous,
    and (b) non-linear solutions in which the item scores are treated as
    ordered-categorical.
	"""
	
	cran = "SINRELEF.LD" 

	version("1.0.3", md5="7eae94ab1b701801b62b83e86ff56ba4")

	depends_on("r@3.5:", type=("build", "run"))
