# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaketools(RPackage):
	"""Exploring and Testing the Toolchain and System Libraries

	Helper functions that interface with the system utilities to learn 
    about the local build environment. Lets you explore 'make' rules to test the
    local configuration, or query 'pkg-config' to find compiler flags and libs 
    needed for building packages with external dependencies. Also contains tools
    to analyze which libraries that a installed R package linked to by inspecting
    output from 'ldd' in combination with information from your distribution 
    package manager, e.g. 'rpm' or 'dpkg'.
	"""
	
	homepage = "https://jeroen.r-universe.dev/maketools"
	cran = "maketools" 

	version("1.3.0", md5="0e2b318283c3454596cd193ad48735aa")
	version("1.2.5", md5="a792501168e79214b43d1fde64f6920c")

	depends_on("r-sys@3.1:", type=("build", "run"))
