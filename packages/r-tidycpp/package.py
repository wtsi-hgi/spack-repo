# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidycpp(RPackage):
	"""Tidy C++ Header-Only Definitions for Parts of the C API of R

	Core parts of the C API of R are wrapped in a C++ namespace via a set
 of inline functions giving a tidier representation of the underlying data structures
 and functionality using a header-only implementation without additional dependencies.
	"""
	
	homepage = "https://github.com/eddelbuettel/tidycpp"
	cran = "tidyCpp" 

	version("0.0.7", md5="7657ac2538dd8d2917d13ee673cabaee")

