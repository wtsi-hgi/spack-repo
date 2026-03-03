# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdnase(RPackage):
	"""Generating Various Numerical Representation Schemes of DNA
Sequences

	Comprehensive toolkit for generating various numerical                                 representation schemes of DNA sequence. The descriptors and similarity
    scores included are extensively used in bioinformatics and chemogenomics.
	"""
	
	homepage = "https://github.com/wind22zhu/rDNAse"
	cran = "rDNAse" 

	version("1.1-1", md5="1f3ad40411e53f2d98e5780722cf5d50")

