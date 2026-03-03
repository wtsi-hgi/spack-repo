# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTipa(RPackage):
	"""Tau-Independent Phase Analysis for Circadian Time-Course Data

	Accurately estimates phase shifts by accounting for period
  changes and for the point in the circadian cycle at which the stimulus occurs.
  See Tackenberg et al. (2018) <doi:10.1177/0748730418768116>.
	"""
	
	homepage = "https://tipa.hugheylab.org"
	cran = "tipa" 

	version("1.0.8", md5="72334f7073d936e24e5f6b24a137b38c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-optimx@2023.8.13:", type=("build", "run"))
