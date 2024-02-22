# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDub(RPackage):
	"""Unpacking Assignment for Lists via Pattern Matching

	Provides an operator for assigning nested components of a list to
  names via a concise pattern matching syntax. This is especially convenient for
  assigning individual names to the multiple values that a function may return
  in the form of a list, and for extracting deeply nested list components.
	"""
	
	homepage = "https://github.com/egnha/dub"
	cran = "dub" 

	version("0.2.0", md5="f1c555ecfc8f8497e49f0474f0b804d9")

