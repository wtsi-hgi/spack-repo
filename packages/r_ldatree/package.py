# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLdatree(RPackage):
	"""Classification Trees with Linear Discriminant Analysis at
Terminal Nodes

	A classification tree method that uses LDA (Linear
    Discriminant Analysis) for variable selection, split determination,
    and model fitting in terminal nodes.  It automatically handles missing
    values and offers visualization tools.
	"""
	
	homepage = "https://github.com/Moran79/LDATree"
	cran = "LDATree" 

	version("0.1.2", md5="311452fdefcbbb83b8980f6f06fd334e")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
