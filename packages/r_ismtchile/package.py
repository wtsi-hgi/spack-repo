# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsmtchile(RPackage):
	"""Calculating Socio Material Territorial Index

	Paquete creado con el fin de facilitar el cálculo y distribución del índice Socio Material Territorial (ISMT), elaborado por el Observatorio de Ciudades UC. La metodología completa está disponible en "ISMT" (<https://ideocuc-ocuc.hub.arcgis.com/datasets/6ed956450cfc4293b7d90df3ce3474e4/about>) [Observatorio de Ciudades UC (2019)]. || Package created to facilitate the calculation and distribution of the Socio-Material Territorial Index by Observatorio de Ciudades UC. The full methodology is available at "ISMT" (<https://ideocuc-ocuc.hub.arcgis.com/datasets/6ed956450cfc4293b7d90df3ce3474e4/about>) [Observatorio de Ciudades UC (2019)].
	"""
	
	cran = "ismtchile" 

	version("2.1.5", md5="f06a86cda4bb11d1dfcf0beec650dc82")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
