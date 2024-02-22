# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKnnp(RPackage):
	"""Time Series Prediction using K-Nearest Neighbors Algorithm
(Parallel)

	Two main functionalities are provided. One of them is predicting values with 
    k-nearest neighbors algorithm and the other is optimizing the parameters k and d of the algorithm.
    These are carried out in parallel using multiple threads.
	"""
	
	homepage = "https://github.com/Grasia/knnp"
	cran = "knnp" 

	version("2.0.0", md5="da1829e1587b5ae5cb270650e835a251")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-paralleldist", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
