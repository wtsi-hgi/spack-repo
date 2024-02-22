# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStratus(RPackage):
	"""Enumeration and Uniform Sampling of Transmission Trees for a
Known Phylogeny

	For a single, known pathogen phylogeny, provides functions for enumeration of the set of compatible epidemic transmission trees, and for uniform sampling from that set. Optional arguments allow for incomplete sampling with a known number of missing individuals, multiple sampling, and known infection time limits. Always assumed are a complete transmission bottleneck and no superinfection or reinfection. See Hall and Colijn (2019) <doi:10.1093/molbev/msz058> for methodology.
	"""
	
	homepage = "http://github.com/mdhall272/STraTUS/"
	cran = "STraTUS" 

	version("1.1.2", md5="fecffb3d39af1354629475c81fdfe17f")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggtree@2:", type=("build", "run"))
	depends_on("r-rcppalgos", type=("build", "run"))
