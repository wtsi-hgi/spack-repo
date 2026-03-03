# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSensitivitymult(RPackage):
	"""Sensitivity Analysis for Observational Studies with Multiple
Outcomes

	Sensitivity analysis for multiple outcomes in observational studies.  For instance, all linear combinations of several outcomes may be explored using Scheffe projections in the comparison() function; see Rosenbaum (2016, Annals of Applied Statistics) <doi:10.1214/16-AOAS942>.  Alternatively, attention may focus on a few principal components in the principal() function.  The package includes parallel methods for individual outcomes, including tests in the senm() function and confidence intervals in the senmCI() function.
	"""
	
	cran = "sensitivitymult" 

	version("1.0.2", md5="f57c379ef8946e25abc6a9c68cc97db4")

