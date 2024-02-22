# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpfp(RPackage):
	"""Fast Implementation of the Iterative Proportional Fitting
Procedure in C

	A fast (C) implementation of the iterative proportional fitting
    procedure.
	"""
	
	homepage = "https://github.com/awblocker/ipfp"
	cran = "ipfp" 

	version("1.0.2", md5="40ddb17abb726b9c3c7f3b50438b65c6")

