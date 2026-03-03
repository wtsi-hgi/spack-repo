# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTosr(RPackage):
	"""Create the Tree of Science from WoS and Scopus

	The goal of 'tosr' is to create the Tree of Science from 
             Web of Science (WoS) and Scopus data. It can read files 
             from both sources at the same time. More information 
             can be found in Valencia-Hernández (2020) 
             <https://revistas.unal.edu.co/index.php/ingeinv/article/view/77718>.
	"""
	
	homepage = "https://github.com/coreofscience/tosr"
	cran = "tosr" 

	version("0.1.4", md5="ad008387a008cf66e9772de16bce23de")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bibliometrix", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rebus", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
