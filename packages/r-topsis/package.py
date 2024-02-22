# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTopsis(RPackage):
	"""TOPSIS method for multiple-criteria decision making (MCDM)

	Evaluation of alternatives based on multiple criteria using TOPSIS method.
	"""
	
	cran = "topsis" 

	version("1.0", md5="07515a51f6f5ca430beca94e75f2ac08")

