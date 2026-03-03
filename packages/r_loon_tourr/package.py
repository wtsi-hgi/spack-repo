# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLoonTourr(RPackage):
	"""Tour in 'Loon'

	Implement tour algorithms in interactive graphical system 'loon'.
	"""
	
	cran = "loon.tourr" 

	version("0.1.3", md5="1ec49b0dadd5492af048499a550761d4")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-loon@1.3.1:", type=("build", "run"))
	depends_on("r-tourr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-loon-ggplot", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
