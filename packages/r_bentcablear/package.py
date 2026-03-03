# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBentcablear(RPackage):
	"""Bent-Cable Regression for Independent Data or Autoregressive
Time Series

	
	Included are two main interfaces, bentcable.ar() and
	bentcable.dev.plot(), for fitting and diagnosing bent-cable
	regressions for autoregressive time-series data (Chiu and
	Lockhart 2010, <doi:10.1002/cjs.10070>) or independent data (time
	series or otherwise - Chiu, Lockhart and Routledge 2006,
	<doi:10.1198/016214505000001177>). Some components in the package
	can also be used as stand-alone functions. The bent cable
	(linear-quadratic-linear) generalizes the broken stick
	(linear-linear), which is also handled by this package. Version
	0.2 corrected a glitch in the computation of confidence intervals
	for the CTP. References that were updated from Versions 0.2.1 and
	0.2.2 appear in Version 0.2.3 and up. Version 0.3.0 improved
	robustness of the error-message producing mechanism. Version 0.3.1
	improves the NAMESPACE file of the package. It is the author's
	intention to distribute any future updates via GitHub.
	"""
	
	cran = "bentcableAR" 

	version("0.3.1", md5="4789fb09f5ae4bf2cbadc801b4c2fdf7")

