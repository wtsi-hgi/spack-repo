# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsymmetryMeasures(RPackage):
	"""Asymmetry Measures for Probability Density Functions

	Provides functions and examples for the weak and strong density asymmetry measures in the articles: "A measure of asymmetry", Patil, Patil and Bagkavos (2012) <doi:10.1007/s00362-011-0401-6> and "A measure of asymmetry based on a new necessary and sufficient condition for symmetry", Patil, Bagkavos and Wood (2014) <doi:10.1007/s13171-013-0034-z>. The measures provided here are useful for quantifying the asymmetry of the shape of a density of a random variable. The package facilitates implementation of the measures which are applicable in a variety of fields including e.g. probability theory, statistics and economics. 
	"""
	
	cran = "asymmetry.measures" 

	version("0.2", md5="c64fb11dc874f2be7f3c2d2d3a97b2c2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
	depends_on("r-skewt", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
