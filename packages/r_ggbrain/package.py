# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgbrain(RPackage):
	"""Create Images of Volumetric Brain Data in NIfTI Format Using
'ggplot2' Syntax

	A 'ggplot2'-consistent approach to generating 2D displays of  volumetric brain imaging data.
  Display data from multiple NIfTI images using standard 'ggplot2' conventions such scales, limits, and
  themes to control the appearance of displays. The resulting plots are returned as 'patchwork' objects,
  inheriting from 'ggplot', allowing for any standard modifications of display aesthetics supported by 'ggplot2'.
	"""
	
	homepage = "https://michaelhallquist.github.io/ggbrain/"
	cran = "ggbrain" 

	version("0.8.1", md5="d9256f4438cd512ed66090f809148c10")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rnifti", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggnewscale", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-imager", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
