# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPreseqr(RPackage):
	"""Predicting Species Accumulation Curves

	Originally as an R version of Preseq <doi:10.1038/nmeth.2375>, the package has extended its functionality to predict the r-species accumulation curve (r-SAC), which is the number of species represented at least r times as a function of the sampling effort. When r = 1, the curve is known as the species accumulation curve, or the library complexity curve in high-throughput genomic sequencing. The package includes both parametric and nonparametric methods, as described by Deng C, et al. (2018) <arXiv:1607.02804v3>. 
	"""
	
	cran = "preseqR" 

	version("4.0.0", md5="b85e80b8b229d743b67d36b312caa5de")

	depends_on("r-polynom", type=("build", "run"))
