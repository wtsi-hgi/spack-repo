# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMdbr(RPackage):
	"""Work with Microsoft Access Files

	Use the open source 'MDB Tools' utilities
    <https://github.com/mdbtools/mdbtools/>. Primarily used for converting
    proprietary Microsoft Access files to simple text files and then
    reading those as data frames.
	"""
	
	homepage = "https://k5cents.github.io/mdbr/"
	cran = "mdbr" 

	version("0.2.1", md5="d89f0723f713af324b7feb0aa2229771")

	depends_on("r-readr", type=("build", "run"))
