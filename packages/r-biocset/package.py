# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiocset(RPackage):
	"""Representing Different Biological Sets

	BiocSet displays different biological sets in a triple tibble format. These three tibbles are `element`, `set`, and `elementset`. The user has the abilty to activate one of these three tibbles to perform common functions from the dplyr package. Mapping functionality and accessing web references for elements/sets are also available in BiocSet.
	"""
	
	bioc = "BiocSet" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BiocSet_1.16.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BiocSet/BiocSet_1.16.1.tar.gz"]

	version("1.16.1", md5="e4724bf36e517a7ef352963200516303")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocio", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-keggrest", type=("build", "run"))
	depends_on("r-ontologyindex", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
