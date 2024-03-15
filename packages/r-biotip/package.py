# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiotip(RPackage):
	"""BioTIP: An R package for characterization of Biological Tipping-Point

	Adopting tipping-point theory to transcriptome profiles to unravel disease regulatory trajectory.
	"""
	
	homepage = "https://github.com/xyang2uchicago/BioTIP"
	bioc = "BioTIP" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BioTIP_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BioTIP/BioTIP_1.16.0.tar.gz"]

	version("1.16.0", md5="9a7765bd55ed7e2d7d09d4eff3b2127c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-scran", type=("build", "run"))
