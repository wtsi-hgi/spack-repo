# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSavvyr(RPackage):
	"""Survival Analysis for AdVerse Events with VarYing Follow-Up
Times

	The SAVVY (Survival Analysis for AdVerse Events with VarYing Follow-Up Times)
    project is a consortium of academic and pharmaceutical
    industry partners that aims to improve the analyses of adverse event (AE)
    data in clinical trials through the use of survival techniques appropriately
    dealing with varying follow-up times and competing events, see
    Stegherr, Schmoor, Beyersmann, et al. (2021) <doi:10.1186/s13063-021-05354-x>.
    Although statistical methodologies have advanced,
    in AE analyses often the incidence proportion, the incidence density or a
    non-parametric Kaplan-Meier estimator are used, which either ignore censoring or
    competing events. This package contains functions to easily conduct the
    proposed improved AE analyses.
	"""
	
	homepage = "https://openpharma.github.io/savvyr/"
	cran = "savvyr" 

	version("0.1.0", md5="3307c4488e1a1056f2e3deef60d862e9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-etm", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
