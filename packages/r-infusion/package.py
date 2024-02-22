# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInfusion(RPackage):
	"""Inference Using Simulation

	Implements functions for simulation-based inference. In particular, implements functions to perform likelihood inference from data summaries whose distributions are simulated. A first approach was described in Rousset et al. (2017 <doi:10.1111/1755-0998.12627>) but the package implements more advanced methods.  
	"""
	
	homepage = "https://www.R-project.org"
	cran = "Infusion" 

	version("2.1.0", md5="c7d62407eca7d4941f72d4e83383a151")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-spamm@4.1.66:", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-blackbox@1.1.41:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
