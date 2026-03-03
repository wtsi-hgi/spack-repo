# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoisbinordnor(RPackage):
	"""Data Generation with Poisson, Binary, Ordinal and Normal
Components

	Generation of multiple count, binary, ordinal and normal variables simultaneously given the marginal characteristics and association structure.
             The details of the method are explained in Demirtas et al. (2012) <DOI:10.1002/sim.5362>.
	"""
	
	cran = "PoisBinOrdNor" 

	version("1.6.3", md5="ba8b998cc10e214f1146d51e402d6b62")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-genord", type=("build", "run"))
