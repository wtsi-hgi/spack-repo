# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNutrinetwork(RPackage):
	"""Structure Learning with Copula Graphical Model

	Statistical tool for learning the structure of direct associations among variables for 
			 continuous data, discrete data and mixed discrete-continuous data. The package is based
			 on the copula graphical model in Behrouzi and Wit (2017) <doi:10.1111/rssc.12287>. 
	"""
	
	cran = "nutriNetwork" 

	version("0.1.2", md5="3944955e52c4f0394fcd65b35654a981")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-huge", type=("build", "run"))
	depends_on("r-tmvtnorm", type=("build", "run"))
