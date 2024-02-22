# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPokemon(RPackage):
	"""Pokemon Data in English and Brazilian Portuguese

	Provides a dataset of Pokemon information in 
  both English and Brazilian Portuguese. The dataset contains 949 rows and 
  22 columns, including information such as the Pokemon's name, ID, height, 
  weight, stats, type, and more.
	"""
	
	homepage = "https://github.com/williamorim/pokemon"
	cran = "pokemon" 

	version("0.1.3", md5="9c6d69ae08433f6fb210bb487892a4fc")

	depends_on("r@2.10:", type=("build", "run"))
