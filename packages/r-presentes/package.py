# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPresentes(RPackage):
	"""Registry of Victims of State Terrorism in Argentina

	Compilation and digitalization of the official registry of victims of state terrorism in Argentina during the last
             military coup. The original data comes from RUVTE-ILID (2019) <https://www.argentina.gob.ar/sitiosdememoria/ruvte/informe> and <http://basededatos.parquedelamemoria.org.ar/registros/>. The title, presentes, comes from present in spanish.
	"""
	
	homepage = "https://diegokoz.github.io/presentes/"
	cran = "presentes" 

	version("0.1.0", md5="8cf8b3a7d1eeecf8d68ca2680d7cd20f")

	depends_on("r@3.5:", type=("build", "run"))
