# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaketools(RPackage):
	"""Exploring and Testing the Toolchain and System Libraries

	A collection of helper functions that interface with the appropriate
    system utilities to learn about the build environment. Lets you explore 'make' 
    rules to test the local configuration, or query 'pkg-config' to find compiler
    flags and libs needed for building packages with external dependencies. Also
    contains tools to analyze which libraries that a installed R package linked to
    by inspecting output from 'ldd' in combination with information from your
    distribution package manager, e.g. 'rpm' or 'dpkg'. Finally the package provides
    Windows-specific utilities to automatically find or install the suitable version
    of the 'Rtools' build environment, and diagnose some common problems.
	"""
	
	homepage = "https://github.com/jeroen/maketools"
	cran = "maketools" 

	version("1.2.5", md5="a792501168e79214b43d1fde64f6920c")

	depends_on("r-sys@3.1:", type=("build", "run"))
