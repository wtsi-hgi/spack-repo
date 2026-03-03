# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfviz(RPackage):
	"""Interactive Visualization Tool for Random Forests

	An interactive data visualization and exploration toolkit
    that implements Breiman and Cutler's original random forest Java based        
    visualization tools in R, for supervised and unsupervised classification and 
    regression within the algorithm random forest. 
	"""
	
	homepage = "https://www.stat.berkeley.edu/~breiman/RandomForests/cc_graphics.htm"
	cran = "rfviz" 

	version("1.0.1", md5="e9968c3a45b1af4c741e3590082b007c")

	depends_on("r@3.5.1:", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-loon", type=("build", "run"))
