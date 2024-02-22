# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvnggrad(RPackage):
	"""Moving Grid Adjustment in Plant Breeding Field Trials

	Package for  moving grid adjustment 
	      in plant breeding field trials.
	"""
	
	cran = "mvngGrAd" 

	version("0.1.6", md5="fdff600a4c8fc1b913963daca64b44fc")

