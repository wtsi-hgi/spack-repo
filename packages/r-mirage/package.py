# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirage(RPackage):
	"""MiRNA Ranking by Gene Expression

	The package contains functions for inferece of target gene regulation by miRNA, based on only target gene expression profile.
	"""
	
	bioc = "MiRaGE" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MiRaGE_1.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MiRaGE/MiRaGE_1.44.0.tar.gz"]

	version("1.50.0", tag="RELEASE_3_21")
	version("1.44.0", sha256="6a622e325a5952b5a4e2be231142da38d7047cfa8ff6e5f2763437fdd8ed81fe")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-biobase@2.23.3:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
