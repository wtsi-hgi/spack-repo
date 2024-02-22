# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLiteranger(RPackage):
	"""Random Forests for Multiple Imputation Based on 'ranger'

	An updated implementation of R package 'ranger' by Wright et al,
    (2017) <doi:10.18637/jss.v077.i01> for training and predicting from random
    forests, particularly suited to high-dimensional data, and for embedding in
    'Multiple Imputation by Chained Equations' (MICE) by van Buuren (2007)
    <doi:10.1177/0962280206074463>. Ensembles of classification and regression
    trees are currently supported. Sparse data of class 'dgCMatrix' (R package
    'Matrix') can be directly analyzed. Conventional bagged predictions are
    available alongside an efficient prediction for MICE via the algorithm
    proposed by Doove et al (2014) <doi:10.1016/j.csda.2013.10.025>. Survival
    and probability forests are not supported in the update, nor is data of
    class 'gwaa.data' (R package 'GenABEL'); use the original 'ranger' package
    for these analyses.
	"""
	
	homepage = "https://github.com/stephematician/literanger"
	cran = "literanger" 

	version("0.0.2", md5="6d6417883696a238b9203d8e94efc586")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-cpp11@0.4.3:", type=("build", "run"))
