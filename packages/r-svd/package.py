# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvd(RPackage):
	"""Interfaces to Various State-of-Art SVD and Eigensolvers

	R bindings to SVD and eigensolvers (PROPACK, nuTRLan).
	"""
	
	homepage = "https://github.com/asl/svd"
	cran = "svd" 

	version("0.5.5", md5="bee5e3da2a81e49b797763fa5467f895")

