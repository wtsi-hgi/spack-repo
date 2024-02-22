# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLtpdvar(RPackage):
	"""LTPD and AOQL Plans for Acceptance Sampling Inspection by
Variables

	Calculation of rectifying LTPD and AOQL plans for sampling inspection by variables which minimize mean inspection cost per lot of process average quality. 
	"""
	
	cran = "LTPDvar" 

	version("1.2.1", md5="0d91c7886ebe1a38c6a8f3f4c02be823")

