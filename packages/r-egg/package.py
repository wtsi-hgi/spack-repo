# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REgg(RPackage):
	"""Extensions for 'ggplot2': Custom Geom, Custom Themes, Plot
Alignment, Labelled Panels, Symmetric Scales, and Fixed Panel
Size

	Miscellaneous functions to help customise 'ggplot2' objects. High-level functions are provided to post-process 'ggplot2' layouts and allow alignment between plot panels, as well as setting panel sizes to fixed values. Other functions include a custom 'geom', and helper functions to enforce symmetric scales or add tags to facetted plots.
	"""
	
	cran = "egg" 

	version("0.4.5", md5="5092b6f00723cee6c47d923780cc781b")

	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
