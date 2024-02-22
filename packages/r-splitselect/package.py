# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSplitselect(RPackage):
	"""Best Split Selection Modeling for Low-Dimensional Data

	Functions to generate or sample from all possible splits of features or variables
             into a number of specified groups. Also computes the best split selection estimator 
             (for low-dimensional data) as defined in Christidis, Van Aelst and Zamar (2019) 
             <arXiv:1812.05678>.
	"""
	
	cran = "splitSelect" 

	version("1.0.3", md5="df2e4c283f2899ee2ef70f2ec6dcb417")

	depends_on("r-multicool", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
