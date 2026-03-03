# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTtutils(RPackage):
	"""Utility Functions

	Contains some auxiliary functions.
	"""
	
	cran = "ttutils" 

	version("1.0-1.1", md5="d44a8ba6b878c608a6b0f09402a64ad4")

