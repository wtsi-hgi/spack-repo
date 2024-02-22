# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBestnormalize(RPackage):
	"""Normalizing Transformation Functions

	Estimate a suite of normalizing transformations, including 
    a new adaptation of a technique based on ranks which can guarantee 
    normally distributed transformed data if there are no ties: ordered 
    quantile normalization (ORQ). ORQ normalization combines a rank-mapping
    approach with a shifted logit approximation that allows
    the transformation to work on data outside the original domain. It is 
    also able to handle new data within the original domain via linear 
    interpolation. The package is built to estimate the best normalizing 
    transformation for a vector consistently and accurately. It implements 
    the Box-Cox transformation, the Yeo-Johnson transformation, three types 
    of Lambert WxF transformations, and the ordered quantile normalization 
    transformation. It estimates the normalization efficacy of other
    commonly used transformations, and it allows users to specify 
    custom transformations or normalization statistics. Finally, functionality
    can be integrated into a machine learning workflow via recipes. 
	"""
	
	homepage = "https://petersonr.github.io/bestNormalize/"
	cran = "bestNormalize" 

	version("1.9.1", md5="496d28a7c8fe29891f04a57bd87b78c0")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-lambertw@0.6.5:", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-recipes", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-butcher", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
