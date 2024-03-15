# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnix(RPackage):
	"""POSIX System Utilities

	Bindings to system utilities found in most Unix systems such as
    POSIX functions which are not part of the Standard C Library.
	"""
	
	homepage = "https://jeroen.r-universe.dev/unix"
	cran = "unix" 

	version("1.5.7", md5="8dec8e89e5276cb5310c4ae23b4fe3ef")

