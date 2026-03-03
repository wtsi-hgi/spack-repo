# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiscretefdr(RPackage):
	"""Multiple Testing Procedures with Adaptation for Discrete Tests

	Multiple testing procedures described in the paper Döhler, Durand and Roquain (2018) "New FDR bounds for discrete and heterogeneous tests" <doi:10.1214/18-EJS1441>. The main procedures of the paper (HSU and HSD), their adaptive counterparts (AHSU and AHSD), and the HBR variant are available and are coded to take as input a set of observed p-values and their discrete support under the null. A function to compute such p-values and supports for Fisher's exact tests is also provided, along with a wrapper allowing to apply discrete procedures directly from contingency tables.
	"""
	
	homepage = "https://github.com/DISOhda/DiscreteFDR"
	cran = "DiscreteFDR" 

	version("1.3.7", md5="44b0456adcb3ae0b6bf175b88b0796ac")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
