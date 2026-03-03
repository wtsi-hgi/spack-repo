# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgbuildr(RPackage):
	"""Save Incremental Builds of Plots

	Saves a 'ggplot' object into multiple files, each with a layer 
    added incrementally. Generally to be used in presentation slides.
    Flexible enough to allow different file types for the final complete plot,
    and intermediate builds.
	"""
	
	cran = "ggbuildr" 

	version("0.1.0", md5="f717f9ee96b1017a9fde6f612d0334de")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
