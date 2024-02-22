# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAstrofns(RPackage):
	"""Astronomy: Time and Position Functions, Misc. Utilities

	Miscellaneous astronomy functions, utilities, and data.
	"""
	
	cran = "astroFns" 

	version("4.2-1", md5="830e3cfc12dce69aa8ba245be6df9563")

