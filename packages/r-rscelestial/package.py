# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRscelestial(RPackage):
	"""Scelestial: Steiner Tree Based Single-Cell Lineage Tree
Inference

	
	Scelestial infers a lineage tree from single-cell DNA mutation matrix. 
	It generates a tree with approximately maximum parsimony through 
	a Steiner tree approximation algorithm. 
	"""
	
	cran = "RScelestial" 

	version("1.0.4", md5="f919c1feacea06fad3c2e0c041fd1992")

	depends_on("r-rcpp", type=("build", "run"))
