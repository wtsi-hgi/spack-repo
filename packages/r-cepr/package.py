# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCepr(RPackage):
	"""Busca CEPs Brasileiros

	
    Retorna detalhes de dados de CEPs brasileiros, bairros, logradouros 
    e tal. (Returns info of Brazilian postal codes, city names, addresses 
    and so on.)
	"""
	
	homepage = "https://github.com/RobertMyles/cepR"
	cran = "cepR" 

	version("0.1.2", md5="cff0c12f74912ab538b576ebd09de5d9")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-httr@1.2.1:", type=("build", "run"))
	depends_on("r-tibble@1.3.3:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-purrr@0.3:", type=("build", "run"))
