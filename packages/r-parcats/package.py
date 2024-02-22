# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParcats(RPackage):
	"""Interactive Parallel Categories Diagrams for 'easyalluvial'

	Complex graphical representations of data are best explored using interactive elements.
  'parcats' adds interactive graphing capabilities to the 'easyalluvial' package.
  The 'plotly.js' parallel categories diagrams offer a good framework for
  creating interactive flow graphs that allow manual drag and drop sorting of dimensions
  and categories, highlighting single flows and displaying mouse over information. The
  'plotly.js' dependency is quite heavy and therefore is outsourced into a separate package.
	"""
	
	homepage = "https://erblast.github.io/parcats/"
	cran = "parcats" 

	version("0.0.5", md5="b856fb199e53ddf89ba59020df3418da")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-easyalluvial@0.2.1:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
