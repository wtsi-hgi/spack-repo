# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgvenn(RPackage):
	"""Draw Venn Diagram by 'ggplot2'

	An easy-to-use way to draw pretty venn diagram by 'ggplot2'.
	"""
	
	cran = "ggvenn" 

	version("0.1.10", md5="eb81af74065bc4f88778e8f88b7bbd8e")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
