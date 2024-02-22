# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCalidad(RPackage):
	"""Assesses the Quality of Estimates Made by Complex Sample Designs

	Assesses the quality of estimates made by complex sample designs,
  following the methodology developed by the National Institute of Statistics Chile (2020, <https://www.ine.cl/docs/default-source/institucionalidad/buenas-pr%C3%A1cticas/clasificaciones-y-estandares/est%C3%A1ndar-evaluaci%C3%B3n-de-calidad-de-estimaciones-publicaci%C3%B3n-27022020.pdf>)
  and by Economic Commission  for Latin America and
  Caribbean (2020, <https://repositorio.cepal.org/bitstream/handle/11362/45681/1/S2000293_es.pdf>). 
	"""
	
	cran = "calidad" 

	version("0.5.0", md5="31549c14f068df33c1ce1231f61120d6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
