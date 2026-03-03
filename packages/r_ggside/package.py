# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgside(RPackage):
	"""Side Grammar Graphics

	The grammar of graphics as shown in 'ggplot2' has provided
  an expressive API for users to build plots. 'ggside' extends 'ggplot2' 
  by allowing users to add graphical information about one of the main panel's
  axis using a familiar 'ggplot2' style API with tidy data. This package is
  particularly useful for visualizing metadata on a discrete axis, or summary
  graphics on a continuous axis such as a boxplot or a density distribution.
	"""
	
	homepage = "https://github.com/jtlandis/ggside"
	cran = "ggside" 

	version("0.3.1", md5="0517315be9a85bb14f87860c767c22b7")
	version("0.2.3", md5="de431757f59fd899e694e7142557ee1e")

	depends_on("r-ggplot2@3.5:", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales@1.3:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
