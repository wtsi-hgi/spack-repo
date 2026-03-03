# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSignibox(RPackage):
	"""Statistical Significance Marks on Boxplots

	Add significance marks to any R Boxplot, including a given significance niveau.
	"""
	
	cran = "signibox" 

	version("1.0", md5="f087f847ab7baf6496bf11222fe3eaa2")

