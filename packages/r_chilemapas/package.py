# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChilemapas(RPackage):
	"""Mapas de las Divisiones Politicas y Administrativas de Chile
(Maps of the Political and Administrative Divisions of Chile)

	Mapas terrestres con topologias simplificadas. Estos mapas no 
  tienen precision geodesica, por lo que aplica el DFL-83 de 1979 de la Republica
  de Chile y se consideran referenciales sin validez legal.
  No se incluyen los territorios antarticos y bajo ningun evento estos mapas
  significan que exista una cesion u ocupacion de territorios soberanos en
  contra del Derecho Internacional por parte de Chile. Esta paquete esta 
  documentado intencionalmente en castellano asciificado para que funcione sin 
  problema en diferentes plataformas.
  (Terrestrial maps with simplified toplogies. These maps lack geodesic
  precision, therefore DFL-83 1979 of the Republic of Chile applies and are
  considered to have no legal validity.
  Antartic territories are excluded and under no event these maps mean
  there is a cession or occupation of sovereign territories against International
  Laws from Chile. This package was intentionally documented in asciified
  spanish to make it work without problem on different platforms.)
	"""
	
	homepage = "https://pacha.dev/chilemapas/"
	cran = "chilemapas" 

	version("0.3.0", md5="eba0568b5e9d52f98788d330b2d701f8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-rmapshaper", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
