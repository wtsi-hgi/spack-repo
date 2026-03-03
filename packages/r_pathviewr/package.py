# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPathviewr(RPackage):
	"""Wrangle, Analyze, and Visualize Animal Movement Data

	Tools to import, clean, and visualize movement data,
    particularly from motion capture systems such as Optitrack's 
    'Motive', the Straw Lab's 'Flydra', or from other sources. We provide 
    functions to remove artifacts, standardize tunnel position and tunnel 
    axes, select a region of interest, isolate specific trajectories, fill
    gaps in trajectory data, and calculate 3D and per-axis velocity. For 
    experiments of visual guidance, we also provide functions that use 
    subject position to estimate perception of visual stimuli. 
	"""
	
	homepage = "https://github.com/ropensci/pathviewr/"
	cran = "pathviewr" 

	version("1.1.7", md5="74457827619c79d941c234f6aeb6e6f0")

	depends_on("r-r-matlab", type=("build", "run"))
	depends_on("r-data-table@1.12.2:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tibble@3.0.1:", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
	depends_on("r-fancova", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-tidyselect@1.1:", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
