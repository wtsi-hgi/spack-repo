# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThgenetics(RPackage):
	"""Genetic Rare Variants Tests

	A step-up test for genetic rare variants in a gene or in a pathway. The method determines an optimal grouping of rare variants analytically. The method has been described in Hoffmann TJ, Marini NJ, and Witte JS (2010) <doi:10.1371/journal.pone.0013584>.
	"""
	
	homepage = "http://sites.google.com/site/thomashoffmannproject/"
	cran = "thgenetics" 

	version("0.4-2", md5="bade2188e8476d736208a43d85be620b")

