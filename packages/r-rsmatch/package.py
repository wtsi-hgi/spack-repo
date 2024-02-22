# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsmatch(RPackage):
	"""Matching Methods for Time-Varying Observational Studies

	Implements popular methods for matching in time-varying
    observational studies. Matching is difficult in this scenario because
    participants can be treated at different times which may have an
    influence on the outcomes. The core methods include: "Balanced Risk
    Set Matching" from Li, Propert, and Rosenbaum (2011)
    <doi:10.1198/016214501753208573> and "Propensity Score Matching with
    Time-Dependent Covariates" from Lu (2005)
    <doi:10.1111/j.1541-0420.2005.00356.x>. Some functions use the
    'Gurobi' optimization back-end to improve the optimization problem
    speed; the 'gurobi' R package and associated software can be
    downloaded from <https://www.gurobi.com> after obtaining a license.
	"""
	
	homepage = "https://skent259.github.io/rsmatch/"
	cran = "rsmatch" 

	version("0.2.1", md5="78cfb1c9da30fc71c52c34b67cada4da")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
