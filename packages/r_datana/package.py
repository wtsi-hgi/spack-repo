# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatana(RPackage):
	"""Data and Functions to Accompany Analisis De Datos Con R

	Datasets and Functions to Accompany Salas-Eljatib (2021, ISBN: 9789566086109) 
    "Analisis de datos con el programa estadistico R: una introduccion aplicada". The package helps carry out data management, exploratory analyses, and model fitting.
	"""
	
	homepage = "https://eljatib.com/rlibro"
	cran = "datana" 

	version("1.0.3", md5="35b99ad0551057b9f4ccbed520529163")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
