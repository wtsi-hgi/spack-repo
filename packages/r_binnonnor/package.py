# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinnonnor(RPackage):
	"""Data Generation with Binary and Continuous Non-Normal Components

	Generation of multiple binary and continuous non-normal variables simultaneously 
             given the marginal characteristics and association structure based on the methodology 
             proposed by Demirtas et al. (2012) <DOI:10.1002/sim.5362>.
	"""
	
	cran = "BinNonNor" 

	version("1.5.3", md5="4544309e3dc12ca44d43dc4e383c148d")

	depends_on("r-bb", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
