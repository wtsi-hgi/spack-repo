# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiodem(RPackage):
	"""Biodemography Functions

	The Biodem package provides a number of functions for Biodemographic analysis.
	"""
	
	cran = "Biodem" 

	version("0.5", md5="e2b27e4db89cd4e3deb32819549581f2")

