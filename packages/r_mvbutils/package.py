# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvbutils(RPackage):
	"""Workspace Organization, Code and Documentation Editing, Package
Prep and Editing, Etc

	Hierarchical workspace tree, code editing and backup, easy package prep, editing of packages while loaded, per-object lazy-loading, easy documentation, macro functions, and miscellaneous utilities. Needed by debug package.
	"""
	
	cran = "mvbutils" 

	version("2.8.232", md5="bacf82532675543def4a0d38890b4d41")

	depends_on("r@3.3:", type=("build", "run"))
