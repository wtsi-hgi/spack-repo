# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSidrar(RPackage):
	"""An Interface to IBGE's SIDRA API

	Allows the user to connect with IBGE's (Instituto Brasileiro de 
    Geografia e Estatistica, see <https://www.ibge.gov.br/> for more information)
    SIDRA API in a flexible way. SIDRA is the acronym to "Sistema IBGE de 
    Recuperacao Automatica" and is the system where IBGE turns available 
    aggregate data from their researches.
	"""
	
	homepage = "https://github.com/rpradosiqueira/sidrar/"
	cran = "sidrar" 

	version("0.2.9", md5="c97e3520a3664c97d55f3afd22f74c04")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
