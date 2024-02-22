# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImmer(RPackage):
	"""Item Response Models for Multiple Ratings

	
    Implements some item response models for multiple
    ratings, including the hierarchical rater model, 
    conditional maximum likelihood estimation of linear 
    logistic partial credit model and a wrapper function
    to the commercial FACETS program. See Robitzsch and
    Steinfeld (2018) for a description of the functionality
    of the package. 
    See Wang, Su and Qiu (2014; <doi:10.1111/jedm.12045>)
    for an overview of modeling alternatives.
	"""
	
	homepage = "https://github.com/alexanderrobitzsch/immer"
	cran = "immer" 

	version("1.4-15", md5="c68ad59952550bb69f710ba0a7edf3f7")

	depends_on("r@3.0.0:", type=("build", "run"))
	depends_on("r-cdm", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-psychotools", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sirt", type=("build", "run"))
	depends_on("r-tam", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
