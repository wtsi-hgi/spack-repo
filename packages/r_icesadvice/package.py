# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcesadvice(RPackage):
	"""Functions Related to ICES Advice

	A collection of functions that facilitate computational steps
  related to advice for fisheries management, according to ICES guidelines.
  These include methods for calculating reference points and model diagnostics.
	"""
	
	homepage = "https://ices.dk/advice"
	cran = "icesAdvice" 

	version("2.1.1", md5="ee89e6ea2f0b9868a608b9f0a817663a")

