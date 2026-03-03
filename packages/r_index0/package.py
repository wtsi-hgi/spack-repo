# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIndex0(RPackage):
	"""Zero-Based Indexing in R

	Extract and replace elements using indices that start from zero (rather than one), as is common in mathematical notation and other programming languages.
	"""
	
	cran = "index0" 

	version("0.0.1", md5="c087c52f6248385d233c95fa6291f468", url="https://cran.r-project.org/src/contrib/index0_0.0.1.tar.gz")

