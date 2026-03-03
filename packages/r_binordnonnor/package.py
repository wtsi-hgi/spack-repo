# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinordnonnor(RPackage):
	"""Concurrent Generation of Binary, Ordinal and Continuous Data

	Generation of samples from a mix of binary, ordinal and continuous random variables with a pre-specified correlation matrix and marginal distributions. The details of the method are explained in Demirtas et al. (2012) <DOI:10.1002/sim.5362>.
	"""
	
	cran = "BinOrdNonNor" 

	version("1.5.2", md5="c5dbb376439ba005ff4ae1e7ca2b0577")

	depends_on("r-genord", type=("build", "run"))
	depends_on("r-ordnor", type=("build", "run"))
	depends_on("r-bb", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
