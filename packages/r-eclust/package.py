# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REclust(RPackage):
	"""Environment Based Clustering for Interpretable Predictive Models
in High Dimensional Data

	Companion package to the paper: An analytic approach for 
    interpretable predictive models in high dimensional data, in the presence of 
    interactions with exposures. Bhatnagar, Yang, Khundrakpam, Evans, Blanchette, Bouchard, Greenwood (2017) <DOI:10.1101/102475>. 
    This package includes an algorithm for clustering high dimensional data that can be affected by an environmental factor. 
	"""
	
	homepage = "https://github.com/sahirbhatnagar/eclust/"
	cran = "eclust" 

	version("0.1.0", md5="11f61e969a055dd427f64d4861e7b802")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dynamictreecut", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-pacman", type=("build", "run"))
	depends_on("r-wgcna", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
