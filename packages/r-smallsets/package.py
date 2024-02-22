# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmallsets(RPackage):
	"""Visual Documentation for Data Preprocessing

	Data practitioners regularly use the 'R' and 'Python' programming languages to 
    prepare data for analyses. Thus, they encode important data preprocessing decisions in 
    'R' and 'Python' code. The 'smallsets' package subsequently decodes these decisions into 
    a Smallset Timeline, a static, compact visualisation of data preprocessing decisions 
    (Lucchesi et al. (2022) <doi:10.1145/3531146.3533175>). The visualisation consists of 
    small data snapshots of different preprocessing steps. The 'smallsets' package builds this 
    visualisation from a user's dataset and preprocessing code located in an 'R', 'R Markdown', 
    'Python', or 'Jupyter Notebook' file. Users simply add structured comments with snapshot  
    instructions to the preprocessing code. One optional feature in 'smallsets' requires 
    installation of the 'Gurobi' optimisation software and 'gurobi' 'R' package, available 
    from <https://www.gurobi.com>. More information regarding the optional feature and 
    'gurobi' installation can be found in the 'smallsets' vignette.
	"""
	
	homepage = "https://lydialucchesi.github.io/smallsets/"
	cran = "smallsets" 

	version("2.0.0", md5="32bd6542fcf087301a968339daa40adf")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggtext", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
