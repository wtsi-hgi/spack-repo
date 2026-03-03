# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreedater(RPackage):
	"""Fast Molecular Clock Dating of Phylogenetic Trees with Rate
Variation

	Functions for estimating times of common ancestry and molecular clock rates of evolution using a variety of evolutionary models, parametric and nonparametric bootstrap confidence intervals, methods for detecting outlier lineages, root-to-tip regression, and a statistical test for selecting molecular clock models. The methods are described in Volz, E.M. and S.D.W. Frost (2017) <doi:10.1093/ve/vex025>.
	"""
	
	cran = "treedater" 

	version("0.5.0", md5="a859e1838674b2f85c12c207c8543e88")

	depends_on("r-ape@5:", type=("build", "run"))
	depends_on("r-limsolve@1.5.5:", type=("build", "run"))
