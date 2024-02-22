# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBhai(RPackage):
	"""Estimate the Burden of Healthcare-Associated Infections

	Provides an approach which is based on the methodology of the Burden of Communicable Diseases in Europe (BCoDE) and can be used for large and small samples such as individual countries. The Burden of Healthcare-Associated Infections (BHAI) is estimated in disability-adjusted life years, number of infections as well as number of deaths per year. Results can be visualized with various plotting functions and exported into tables.
	"""
	
	cran = "BHAI" 

	version("0.99.2", md5="697d853c96e60ac493fd1590720d094e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-prevtoinc", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
