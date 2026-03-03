# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyheatmaps(RPackage):
	"""Heatmaps from Tidy Data

	The goal of 'tidyheatmaps' is to simplify the generation of publication-ready heatmaps from tidy data. By offering an interface to the powerful 'pheatmap' package, it allows for the effortless creation of intricate heatmaps with minimal code.
	"""
	
	homepage = "https://github.com/jbengler/tidyheatmaps"
	cran = "tidyheatmaps" 

	version("0.2.1", md5="0b2414b2588bd512f1bbd22bb7d377c2")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
