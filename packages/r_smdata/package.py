# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmdata(RPackage):
	"""Data to Accompany Smithson & Merkle, 2013

	Contains data files to accompany Smithson & Merkle (2013), Generalized Linear Models for Categorical and Continuous Limited Dependent Variables.
	"""
	
	cran = "smdata" 

	version("1.2", md5="2fec3aef46db1839e64adb08f1a430f0")

