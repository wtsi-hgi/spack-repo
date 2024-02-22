# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbseil(RPackage):
	"""'C++' Header Files from 'Abseil'

	Wraps the 'Abseil' 'C++' library for use by R packages.
    Original files are from <https://github.com/abseil/abseil-cpp>.
    Patches are located at
    <https://github.com/doccstat/abseil-r/tree/main/local/patches>.
	"""
	
	homepage = "https://abseil.xingchi.li"
	cran = "abseil" 

	version("2023.8.2.1", md5="9b5fade0669c69580d4728a6e5da02e5")

