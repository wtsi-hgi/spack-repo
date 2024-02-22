# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RListarray(RPackage):
	"""Incomplete Array with Arbitrary R Objects as Indices

	The aim of the package is to create data objects which allow for accesses like x["test"] and x["test","test"].
	"""
	
	cran = "listArray" 

	version("0.1.1", md5="f795a7f5c9e988e60c01175a9bace877")

