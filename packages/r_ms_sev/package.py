# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsSev(RPackage):
	"""Package for Calculation of ARMSS, Local MSSS and Global MSSS

	Calculates ARMSS (age related multiple sclerosis severity), and both local and global MSSS (multiple sclerosis severity score).
	"""
	
	cran = "ms.sev" 

	version("1.0.4", md5="8d8d89811ab5ddeac1d7c028e8f0274b")

