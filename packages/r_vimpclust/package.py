# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVimpclust(RPackage):
	"""Variable Importance in Clustering

	An implementation of methods related to sparse clustering and variable importance 
    in clustering. The package currently allows to perform sparse k-means clustering with a group 
    penalty, so that it automatically selects groups of numerical features. It also allows to 
    perform sparse clustering and variable selection on mixed data (categorical and numerical 
    features), by preprocessing each categorical feature as a group of numerical features.
    Several methods for visualizing and exploring the results are also provided. 
    M. Chavent, J. Lacaille, A. Mourer and M. Olteanu (2020)<https://www.esann.org/sites/default/files/proceedings/2020/ES2020-103.pdf>.
	"""
	
	cran = "vimpclust" 

	version("0.1.0", md5="996761caa1572218e4ebb6ce4142b310")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pcamixdata", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-polychrome", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
