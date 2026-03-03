# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSubdetect(RPackage):
	"""Detect Subgroup with an Enhanced Treatment Effect

	A test for the existence of a subgroup with enhanced treatment 
    effect. And, a sample size calculation procedure for the subgroup 
    detection test.
	"""
	
	cran = "subdetect" 

	version("1.2", md5="e6213f05ccd95b0a213be4ea75fdfc68")

