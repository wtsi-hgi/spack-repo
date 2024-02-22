# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSuggests(RPackage):
	"""Declare when Suggested Packages are Needed

	By adding dependencies to the "Suggests" field of a package's
    DESCRIPTION file, and then declaring that they are needed within any
    dependent functionality, it is often possible to significantly reduce the
    number of "hard" dependencies required by a package. This package provides
    a minimal way to declare when a suggested package is needed.
	"""
	
	homepage = "https://github.com/owenjonesuob/suggests"
	cran = "suggests" 

	version("0.1.0", md5="0c10600f74fa0d276f6e8868b1233938")

