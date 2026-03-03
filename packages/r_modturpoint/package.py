# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModturpoint(RPackage):
	"""Estimate ED50 Based on Modified Turning Point Method

	Turning point method is a method proposed by Choi (1990) <doi:10.2307/2531453> to 
    estimate 50 percent effective dose (ED50) in the study of drug sensitivity. The method has 
    its own advantages for that it can provide robust ED50 estimation. This package contains 
    the modified function of Choi's turning point method.
	"""
	
	cran = "modTurPoint" 

	version("0.1.0", md5="67d7a2d14753e03cf975b9304ba26ba6")

