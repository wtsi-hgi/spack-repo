# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpinar(RPackage):
	"""Argentina's Public Opinion Toolbox

	A toolbox for working with public opinion data from Argentina. It facilitates access to microdata and the calculation of indicators of the Trust in Government Index (ICG), prepared by the Torcuato Di Tella University. Although we will try to document everything possible in English, by its very nature Spanish will be the main language. El paquete fue pensado como una caja de herramientas para el trabajo con datos de opinión pública de Argentina. El mismo  facilita el acceso a los microdatos y el cálculos de indicadores del Índice de Confianza en el Gobierno (ICG), elaborado por la Universidad Torcuato Di Tella.
	"""
	
	homepage = "https://github.com/PoliticaArgentina/opinAr"
	cran = "opinAr" 

	version("1.0.0", md5="5f6a33a6b3be1765fd2296eb652bda38")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sjplot", type=("build", "run"))
	depends_on("r-gt", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
