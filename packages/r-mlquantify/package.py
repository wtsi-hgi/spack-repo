# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlquantify(RPackage):
	"""Algorithms for Class Distribution Estimation

	Quantification is a prominent machine learning task that has received an 
    increasing amount of attention in the last years. The objective is to predict the 
    class distribution of a data sample. This package is a collection of machine learning 
    algorithms for class distribution estimation. This package include algorithms from
    different paradigms of quantification. These methods are described in the paper: 
    A. Maletzke, W. Hassan, D. dos Reis, and G. Batista. The importance of the test set 
    size in quantification assessment. In Proceedings of the Twenty-Ninth International 
    Joint Conference on Artificial Intelligence, IJCAI20, pages 2640–2646, 2020.
    <doi:10.24963/ijcai.2020/366>.
	"""
	
	homepage = "https://github.com/andregustavom/mlquantify"
	cran = "mlquantify" 

	version("0.2.0", md5="5c14c1e863d2db66a5db4d4fab4773d3")

	depends_on("r-caret", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
