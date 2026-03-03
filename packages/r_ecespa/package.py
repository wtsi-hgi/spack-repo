# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcespa(RPackage):
	"""Functions for Spatial Point Pattern Analysis

	Some wrappers, functions and data sets for for spatial point pattern analysis (mainly based on 'spatstat'), used in the book "Introduccion al Analisis Espacial de Datos en Ecologia y Ciencias Ambientales: Metodos y Aplicaciones" and in the papers by De la Cruz et al. (2008) <doi:10.1111/j.0906-7590.2008.05299.x> and Olano et al. (2009) <doi:10.1051/forest:2008074>.
	"""
	
	cran = "ecespa" 

	version("1.1-17", md5="b27382a0e0762d8089db50880f07007b")

	depends_on("r-spatstat@2.0.0:", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-spatstat-model", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
