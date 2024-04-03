# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMagmaclustr(RPackage):
	"""Clustering and Prediction using Multi-Task Gaussian Processes
with Common Mean

	An implementation for the multi-task Gaussian processes with common 
    mean framework. Two main algorithms, called 'Magma' and 'MagmaClust', 
    are available to perform predictions for supervised learning problems, in
    particular for time series or any functional/continuous data applications.
    The corresponding articles has been respectively proposed by Arthur Leroy, 
    Pierre Latouche, Benjamin Guedj and Servane Gey (2022) 
    <doi:10.1007/s10994-022-06172-1>, and Arthur Leroy, Pierre Latouche, 
    Benjamin Guedj and Servane Gey (2023) <https://jmlr.org/papers/v24/20-1321.html>.
    Theses approaches leverage the learning of cluster-specific mean processes,
    which are common across similar tasks, to provide enhanced prediction
    performances (even far from data) at a linear computational cost (in
    the number of tasks).  'MagmaClust' is a generalisation of 'Magma'
    where the tasks are simultaneously clustered into groups, each being
    associated to a specific mean process.  User-oriented functions in the
    package are decomposed into training, prediction and plotting
    functions. Some basic features (classic kernels, training, prediction) of
    standard Gaussian processes are also implemented. 
	"""
	
	homepage = "https://github.com/ArthurLeroy/MagmaClustR"
	cran = "MagmaClustR" 

	version("1.2.0", md5="915e4a56880600b6b735102ff82ffed5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
