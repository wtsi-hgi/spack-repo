# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeovol(RPackage):
	"""Geopolitical Volatility (GEOVOL) Modelling

	Simulation, estimation and inference for the geopolitical volatility (GEOVOL) model of Engle and Campos-Martins (2020) <doi:10.2139/ssrn.3685213>, where GEOVOL is modelled as a latent multiplicative volatility factor with heterogeneous factor loadings. Estimation is carried out as a maximization-maximization procedure, where GEOVOL and the GEOVOL loadings are estimated iteratively until convergence.
	"""
	
	homepage = "https://sites.google.com/site/susanacamposmartins/"
	cran = "geovol" 

	version("1.0", md5="38841295be5e371b36c0e46013f24c1f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
