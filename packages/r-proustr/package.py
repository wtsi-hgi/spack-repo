# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProustr(RPackage):
	"""Tools for Natural Language Processing in French

	Tools for Natural Language Processing in French and texts from Marcel Proust's collection 
  "A La Recherche Du Temps Perdu". The novels contained in this collection are 
  "Du cote de chez Swann ", "A l'ombre des jeunes filles en fleurs","Le Cote de Guermantes", 
  "Sodome et Gomorrhe I et II", "La Prisonniere", "Albertine disparue", and "Le Temps retrouve".
	"""
	
	homepage = "https://github.com/ColinFay/proustr"
	cran = "proustr" 

	version("0.4.0", md5="90c3c777986b04f582936d504e7686d3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tokenizers", type=("build", "run"))
	depends_on("r-snowballc", type=("build", "run"))
	depends_on("r-attempt", type=("build", "run"))
