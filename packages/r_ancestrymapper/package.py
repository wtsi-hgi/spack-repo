# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAncestrymapper(RPackage):
	"""Assigning Ancestry Based on Population References

	Assigns genetic ancestry to an individual and
	studies relationships between local and global populations.
	"""
	
	cran = "AncestryMapper"

	version("2.0", md5="bef31a5015a0af1a6702cbb35df1fc29")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-svd@0.3.3.2:", type=("build", "run"))
