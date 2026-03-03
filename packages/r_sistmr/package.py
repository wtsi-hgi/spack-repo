# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSistmr(RPackage):
	"""A Collection of Utility Function from the Inserm/Inria SISTM
Team

	Functions common to members of the SISTM team.
	"""
	
	cran = "sistmr" 

	version("0.1.1", md5="3c9c341eab1a20757736c3f96d99ab11")

	depends_on("r-blandaltmanleh", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggbeeswarm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
