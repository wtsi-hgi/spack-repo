# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNhsnumber(RPackage):
	"""Tools for Working with NHS Number Checksums

	Provides functions for working with NHS number checksums.
    The UK's National Health Service issues NHS numbers to all users of its
    services and this package implements functions for verifying that the
    numbers are valid according to the checksum scheme the NHS use.
    Numbers can be validated and checksums created.
	"""
	
	homepage = "https://github.com/sellorm/nhsnumber"
	cran = "nhsnumber" 

	version("0.1.2", md5="94d105e1269922b8bfba3aaba6a2c666")

