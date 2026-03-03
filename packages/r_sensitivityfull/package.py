# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSensitivityfull(RPackage):
	"""Sensitivity Analysis for Full Matching in Observational Studies

	Sensitivity to unmeasured biases in an observational study that is a full match.  Function senfm() performs tests and function senfmCI() creates confidence intervals.  The method uses Huber's M-statistics, including least squares, and is described in Rosenbaum (2007, Biometrics) <DOI:10.1111/j.1541-0420.2006.00717.x>.
	"""
	
	cran = "sensitivityfull" 

	version("1.5.6", md5="0630abd41a2a9a9eb70ae090fcebb0ed")

