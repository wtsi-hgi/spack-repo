# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParmigene(RPackage):
	"""Parallel Mutual Information Estimation for Gene Network
Reconstruction

	Parallel estimation of the mutual information based on entropy
    estimates from k-nearest neighbors distances and algorithms for the
    reconstruction of gene regulatory networks
    (Sales et al, 2011 <doi:10.1093/bioinformatics/btr274>).
	"""
	
	homepage = "https://github.com/sales-lab/parmigene"
	cran = "parmigene" 

	version("1.1.0", md5="b4e0213cf464ca63b6dc51f3133c975a")

