# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBicare(RPackage):
	"""Biclustering Analysis and Results Exploration

	Biclustering Analysis and Results Exploration.
	"""
	
	homepage = "http://bioinfo.curie.fr"
	bioc = "BicARE" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BicARE_1.60.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BicARE/BicARE_1.60.0.tar.gz"]

	version("1.66.0", tag="RELEASE_3_21")
	version("1.60.0", sha256="30fd6ff9fef0df03a78578b9ae3dcb59f7cf8b9c9cf13300ba6d561668e73682")

	depends_on("r@1.8:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
