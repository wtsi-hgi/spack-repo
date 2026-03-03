# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVinecopula(RPackage):
	"""Statistical Inference of Vine Copulas

	Provides tools for the statistical analysis of regular vine copula 
    models, see Aas et al. (2009) <doi:10.1016/j.insmatheco.2007.02.001> and 
    Dissman et al. (2013) <doi:10.1016/j.csda.2012.08.010>.
    The package includes tools for parameter estimation, model selection,
    simulation, goodness-of-fit tests, and visualization. Tools for estimation,
    selection and exploratory data analysis of bivariate copula models are also
    provided.
	"""
	
	homepage = "https://github.com/tnagler/VineCopula"
	cran = "VineCopula" 

	version("2.5.0", md5="be42b12b7061fa6a6a677096ef05e3c3")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-adgoftest", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
