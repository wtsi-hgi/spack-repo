# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLest(RPackage):
	"""Vectorised Nested if-else Statements Similar to CASE WHEN in
'SQL'

	Functions for vectorised conditional recoding of
    variables. case_when() enables you to vectorise multiple if and else
    statements (like 'CASE WHEN' in 'SQL'). if_else() is a stricter and
    more predictable version of ifelse() in 'base' that preserves
    attributes. These functions are forked from 'dplyr' with all package
    dependencies removed and behave identically to the originals.
	"""
	
	cran = "lest" 

	version("1.1.0", md5="ada5ed3564479335dc027838ad8e840f")

