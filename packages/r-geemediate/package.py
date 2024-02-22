# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeemediate(RPackage):
	"""Mediation Analysis for Generalized Linear Models Using the
Difference Method

	Causal mediation analysis for a single exposure/treatment and a
    single mediator, both allowed to be either continuous or binary. The package
    implements the difference method and provides point and interval estimates as
    well as testing for the natural direct and indirect effects and the mediation
    proportion. Nevo, Xiao and Spiegelman (2017) <doi:10.1515/ijb-2017-0006>.
	"""
	
	cran = "GEEmediate" 

	version("1.1.4", md5="1146662c126b8edf9fe79fbc5e9f96b1")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-gee", type=("build", "run"))
