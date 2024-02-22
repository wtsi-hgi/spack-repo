# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIapws95(RPackage):
	"""Thermophysical Properties of Water and Steam

	An implementation of the International Association for the
    Properties of Water (IAPWS) Formulation 1995 for the Thermodynamic Properties of Ordinary
    Water Substance for General and Scientific Use and on the releases for viscosity,
    conductivity, surface tension and melting pressure.
	"""
	
	cran = "IAPWS95" 

	version("1.2.4", md5="db852998561af6cfffcb011d30a5754f", url="https://cran.r-project.org/src/contrib/IAPWS95_1.2.4.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
