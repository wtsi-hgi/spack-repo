# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMfag(RPackage):
	"""Multiple Factor Analysis (MFA)

	Performs Multiple Factor Analysis method for quantitative, categorical, frequency and mixed data, in addition to generating a lot of graphics, also has other useful functions.
	"""
	
	cran = "MFAg" 

	version("1.9", md5="db8b836d099e3b01dba5688a6d9feae5")

