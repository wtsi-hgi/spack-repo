# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REgor(RPackage):
	"""Import and Analyse Ego-Centered Network Data

	Tools for importing, analyzing and visualizing ego-centered
    network data. Supports several data formats, including the export formats of
    'EgoNet', 'EgoWeb 2.0' and 'openeddi'. An interactive (shiny) app for the
    intuitive visualization of ego-centered networks is provided. Also included
    are procedures for creating and visualizing Clustered Graphs 
    (Lerner 2008 <DOI:10.1109/PACIFICVIS.2008.4475458>).
	"""
	
	homepage = "https://github.com/tilltnet/egor"
	cran = "egor" 

	version("1.24.2", md5="338f08b4a8b55ba353ff007747b99bd2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
	depends_on("r-srvyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
