# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiatsm(RPackage):
	"""Multicountry Term Structure of Interest Rates Models

	Estimation routines for several classes of affine term structure of interest rates models. All the models are based on the single-country unspanned macroeconomic risk framework from Joslin, Priebsch, and Singleton (2014) <doi:10.1111/jofi.12131>. Multicountry extensions such as the ones of Jotikasthira, Le, and Lundblad (2015) <doi:10.1016/j.jfineco.2014.09.004>, Candelon and Moura (2021) <http://hdl.handle.net/2078.1/249985>, and Candelon and Moura (2023) <doi:10.1016/j.econmod.2023.106453> are also available. 
	"""
	
	cran = "MultiATSM" 

	version("0.3.5", md5="79bd68ee58ed325dd7dc0e9256455bc2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-wrapr", type=("build", "run"))
	depends_on("r-hablar", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
