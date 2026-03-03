# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovidmx(RPackage):
	"""Descarga y analiza datos de COVID-19 en México

	Herramientas para el análisis de datos de COVID-19 en México. Descarga y analiza 
  los datos para COVID-19 de la Direccion General de Epidemiología de México (DGE) 
  <https://www.gob.mx/salud/documentos/datos-abiertos-152127>,
  la Red de Infecciones Respiratorias Agudas Graves (Red IRAG)
  <https://www.gits.igg.unam.mx/red-irag-dashboard/reviewHome> y la Iniciativa Global 
  para compartir todos los datos de influenza (GISAID)
  <https://gisaid.org/>. 
  English: Downloads and analyzes data  of COVID-19 from the  Mexican General 
  Directorate of Epidemiology (DGE), the Network of 
  Severe Acute Respiratory  Infections (IRAG network),and the Global 
  Initiative on Sharing All Influenza Data GISAID.
	"""
	
	homepage = "https://github.com/RodrigoZepeda/covidmx"
	cran = "covidmx" 

	version("0.7.7", md5="f599352f331970c5401c41f42352c916")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-duckdb@0.4:", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-pins@1.0.1:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
