# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwag(RPackage):
	"""Sparse Wrapper Algorithm

	An algorithm that trains a meta-learning procedure that combines 
    screening and wrapper methods to find a set of extremely low-dimensional attribute 
    combinations. This package works on top of the 'caret' package and proceeds in a 
    forward-step manner. More specifically, it builds and tests learners starting 
    from very few attributes until it includes a maximal number of attributes by 
    increasing the number of attributes at each step. Hence, for each fixed number
    of attributes, the algorithm tests various (randomly selected) learners and 
    picks those with the best performance in terms of training error. Throughout,
    the algorithm uses the information coming from the best learners at the previous
    step to build and test learners in the following step. In the end, it outputs
    a set of strong low-dimensional learners.
	"""
	
	homepage = "https://github.com/SMAC-Group/SWAG-R-Package/"
	cran = "swag" 

	version("0.1.0", md5="23a57379afd2582a1f6c7e12b0fb807c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
