# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMisha(RPackage):
	"""Toolkit for Analysis of Genomic Data

	A toolkit for analysis of genomic data. The 'misha' package
    implements an efficient data structure for storing genomic data, and
    provides a set of functions for data extraction, manipulation and
    analysis. Some of the 2D genome algorithms were described in Yaffe and Tanay
    (2011) <doi:10.1038/ng.947>. 
	"""
	
	homepage = "https://tanaylab.github.io/misha/"
	cran = "misha" 

	version("4.2.9", md5="f73c374aee99f1227489dd98f7436abd")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
