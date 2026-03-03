# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeclared(RPackage):
	"""Functions for Declared Missing Values

	A zero dependency package containing functions to declare labels
    and missing values, coupled with associated functions to create (weighted)
    tables of frequencies and various other summary measures. 
    Some of the base functions have been rewritten to make use of the specific 
    information about the missing values, most importantly to distinguish
    between empty NA and declared NA values.
    Some functions have similar functionality with the corresponding ones from
    packages "haven" and "labelled". The aim is to ensure as much compatibility
    as possible with these packages, while offering an alternative in the
    objects of class "declared".
	"""
	
	homepage = "https://github.com/dusadrian/declared"
	cran = "declared" 

	version("0.24", md5="8e4b4c9ec6d14931e86812b9f6544f91")

