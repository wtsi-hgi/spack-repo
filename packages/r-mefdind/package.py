# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMefdind(RPackage):
	"""Imports Data from MoE Spain

	
  Imports indicator data provided by the Ministry of Education (MoE),Spain. 
  The data is stored at <https://www.educacionyfp.gob.es/servicios-al-ciudadano/estadisticas/no-universitaria.html>
  Includes functions for reading, downloading, and selecting data
  for main series. This package is not sponsored or supported by the MoE Spain.  
  Importa datos con indicadores del Ministerio de Educación y Formación Profesional (MEFD) de Españá. 
  Los datos están en <https://www.educacionyfp.gob.es/servicios-al-ciudadano/estadisticas/no-universitaria.html>
  Contiene funciones para leer, descargar, y seleccionar bases de datos de series principales.
  Este paquete no es patrocinado o respaldado por el MEFD.  
	"""
	
	homepage = "https://eldafani.github.io/mefdind/"
	cran = "mefdind" 

	version("0.1", md5="4f112fccb5fccfe5babbb63c008ec53d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
