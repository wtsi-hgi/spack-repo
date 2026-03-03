# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REstadistica(RPackage):
	"""Fundamentos De Estadistica Descriptiva e Inferencial

	Este paquete pretende apoyar el proceso enseñanza-aprendizaje de estadística descriptiva e inferencial. Las funciones contenidas en el paquete 'estadistica' cubren los conceptos básicos estudiados en un curso introductorio. Muchos conceptos son ilustrados con gráficos dinámicos o web apps para facilitar su comprensión. This package aims to help the teaching-learning process of descriptive and inferential statistics. The functions contained in the package 'estadistica' cover the basic concepts studied in a statistics introductory course. Many concepts are illustrated with dynamic graphs or web apps to make the understanding easier. See: Esteban et al. (2005, ISBN: 9788497323741), Newbold et al.(2019, ISBN:9781292315034 ), Murgui et al. (2002, ISBN:9788484424673) .
	"""
	
	homepage = "https://www.uv.es/estadistic/"
	cran = "estadistica" 

	version("0.2.3", md5="d472ae9a302dd91d46e9cafac935968a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rio", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
