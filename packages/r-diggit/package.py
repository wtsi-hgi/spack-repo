# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiggit(RPackage):
	"""Inference of Genetic Variants Driving Cellular Phenotypes

	Inference of Genetic Variants Driving Cellullar Phenotypes by the DIGGIT algorithm
	"""
	
	bioc = "diggit" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/diggit_1.34.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/diggit/diggit_1.34.0.tar.gz"]

	version("1.34.0", md5="8685d9b55ebfad0b44d6ca96d6fb4ab0")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-viper@1.3.1:", type=("build", "run"))
