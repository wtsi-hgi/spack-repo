# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmost(RPackage):
	"""Estimates Pareto-Optimal Solution for Hiring with 3 Objectives

	Estimates Pareto-optimal solution for personnel selection
    with 3 objectives using Normal Boundary Intersection (NBI) algorithm
    introduced by Das and Dennis (1998) <doi:10.1137/S1052623496307510>.
    Takes predictor intercorrelations and predictor-objective relations as
    input and generates a series of solutions containing predictor weights
    as output. Accepts between 3 and 10 selection predictors. Maximum 2
    objectives could be adverse impact objectives. Partially modeled after
    De Corte (2006) TROFSS Fortran program
    <https://users.ugent.be/~wdecorte/trofss.pdf> and updated from
    'ParetoR' package described in Song et al. (2017)
    <doi:10.1037/apl0000240>. For details, see Study 3 of Zhang et al. (2023).
	"""
	
	cran = "rMOST" 

	version("1.0.1", md5="05d0a4a42612cbb75e99877525015252")

	depends_on("r-nloptr", type=("build", "run"))
