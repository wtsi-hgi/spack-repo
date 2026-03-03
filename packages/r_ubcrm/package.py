# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUbcrm(RPackage):
	"""Functions to Simulate and Conduct Dose-Escalation Phase I
Studies

	Two Phase I designs are implemented in the package: the classical 3+3 and the Continual Reassessment Method. Simulations tools are also available to estimate the operating characteristics of the methods with several user-dependent options.
	"""
	
	cran = "UBCRM" 

	version("1.0.2", md5="857853001c2804d4a671fdc4c3e8fb50")

