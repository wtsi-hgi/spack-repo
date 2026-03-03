# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetsyn(RPackage):
	"""Interface with the Meteo France Synop Data API

	Provides an interface with the Meteo France Synop data API 
    (see <https://donneespubliques.meteofrance.fr/?fond=produit&id_produit=90&id_rubrique=32> 
    for more information). 
    The Meteo France Synop data are made of meteorological data recorded 
    every three hours on 62 French meteorological stations. 
	"""
	
	homepage = "https://github.com/paulponcet/metsyn"
	cran = "metsyn" 

	version("0.1.2", md5="b7e2f2981c5a7176de361c799193f46c")

	depends_on("r@3.1.3:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
