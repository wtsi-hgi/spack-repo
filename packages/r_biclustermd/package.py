# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiclustermd(RPackage):
	"""Biclustering with Missing Data

	Biclustering is a statistical learning technique that simultaneously 
    partitions and clusters rows and columns of a data matrix. Since the solution 
    space of biclustering is in infeasible to completely search with current 
    computational mechanisms, this package uses a greedy heuristic. The algorithm 
    featured in this package is, to the best our knowledge, the first biclustering 
    algorithm to work on data with missing values. Li, J., Reisner, J., Pham, H., 
    Olafsson, S., and Vardeman, S. (2020) Biclustering with Missing Data. Information 
    Sciences, 510, 304–316.
	"""
	
	homepage = "https://github.com/jreisner/biclustermd"
	cran = "biclustermd" 

	version("0.2.3", md5="df8270e142de34317dd4842e8850ca55")

	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tidyr@0.8.1:", type=("build", "run"))
	depends_on("r-biclust@2.0.1:", type=("build", "run"))
	depends_on("r-doparallel@1.0.14:", type=("build", "run"))
	depends_on("r-dplyr@0.7.6:", type=("build", "run"))
	depends_on("r-foreach@1.4.4:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-nycflights13@1:", type=("build", "run"))
	depends_on("r-phyclust@0.1.24:", type=("build", "run"))
