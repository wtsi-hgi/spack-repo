# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLifttest(RPackage):
	"""A Bootstrap Proportion Test for Brand Lift Testing

	A bootstrap proportion test for Brand Lift Testing to quantify the effectiveness of online advertising. Methods of the bootstrap proportion test are presented in
    Liu, Yu, Mao, Wu, Dyer (2023) <doi:10.1145/3583780.3615021>.
	"""
	
	cran = "LiftTest" 

	version("0.2.0", md5="9463c5587f093f40ba15bf0236ec18f2")

