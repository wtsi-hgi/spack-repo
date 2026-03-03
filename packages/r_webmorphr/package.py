# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWebmorphr(RPackage):
	"""Reproducible Stimuli

	Create reproducible image stimuli, 
    specialised for face images with 'psychomorph' or 'webmorph' templates.
	"""
	
	homepage = "https://debruine.github.io/webmorphR/"
	cran = "webmorphR" 

	version("0.1.1", md5="4885191b672a1eccc84aad8d2dfd4f47")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-geomorph", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rsvg", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
