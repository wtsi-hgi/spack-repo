# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMnet(RPackage):
	"""Modeling Group Differences and Moderation Effects in Statistical
Network Models

	A toolbox for modeling manifest and latent group differences and moderation effects in various statistical network models.
	"""
	
	cran = "mnet" 

	version("0.1.2", md5="c8d3d1062dbae6cebc3b3c53328fe6cd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mlvar", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
