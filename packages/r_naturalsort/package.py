# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNaturalsort(RPackage):
	"""Natural Ordering

	Provides functions related to human natural ordering.
    It handles adjacent digits in a character sequence as a number so that
    natural sort function arranges a character vector by their numbers, not digit
    characters. It is typically seen when operating systems lists file names. For
    example, a sequence a-1.png, a-2.png, a-10.png looks naturally ordered because 1
    < 2 < 10 and natural sort algorithm arranges so whereas general sort algorithms
    arrange it into a-1.png, a-10.png, a-2.png owing to their third and fourth
    characters.
	"""
	
	cran = "naturalsort" 

	version("0.1.3", md5="9c705ea6e3033ed186b3d4932e2ae0c1")

