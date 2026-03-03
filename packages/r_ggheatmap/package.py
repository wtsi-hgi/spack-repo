# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgheatmap(RPackage):
	"""Plot Heatmap

	The flexibility and excellence of 'ggplot2' is unquestionable, 
    so many drawing tools basically need 'ggplot2' as the operating object. 
    In order to develop a heatmap drawing system based on ggplot2, we developed 
    this tool, mainly to solve the heatmap puzzle problem and the flexible 
    connection between the heatmap and the 'ggplot2' object.
    The advantages of this tool are as follows: 
    1. More flexible label settings; 
    2. Realize the linkage of heatmap and 'ggplot2' drawing system, 
       which is helpful for operations such as puzzles; 
    3. Simple and easy to operate; 
    4. Optimization of clustering tree visualization.
	"""
	
	cran = "ggheatmap" 

	version("2.2", md5="23cb5a71813c350fecca10351af70ce6")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-aplot", type=("build", "run"))
	depends_on("r-factoextra", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
