# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtapas(RPackage):
	"""Random Tanglegram Partitions

	Applies a given global-fit method to random partial tanglegrams of a fixed size
             to identify the associations, terminals, and nodes that maximize phylogenetic
             (in)congruence. It also includes functions to compute more easily the confidence
             intervals of classification metrics and plot results, reducing computational time.
             See Llaberia-Robledillo et al. (2022, <doi:10.1101/2022.05.17.492291>).
	"""
	
	cran = "Rtapas" 

	version("1.1", md5="731c0b703d5973af906f70386b93a90e")

	depends_on("r-phytools", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-distory", type=("build", "run"))
	depends_on("r-giniwegneg", type=("build", "run"))
	depends_on("r-paco", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-parallelly", type=("build", "run"))
