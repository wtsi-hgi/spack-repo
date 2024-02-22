# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinnor(RPackage):
	"""Simultaneous Generation of Multivariate Binary and Normal
Variates

	Generating multiple binary and normal variables simultaneously given marginal characteristics and association structure based on the methodology proposed by Demirtas and Doganay (2012) <DOI:10.1080/10543406.2010.521874>.
	"""
	
	cran = "BinNor" 

	version("2.3.3", md5="6e442d16e5701e72084494ab88973ba9")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
