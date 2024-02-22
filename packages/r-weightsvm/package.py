# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeightsvm(RPackage):
	"""Subject Weighted Support Vector Machines

	Functions for subject/instance weighted support vector machines (SVM). 
    It uses a modified version of 'libsvm' and is compatible with package 'e1071'. It also allows user defined kernel matrix.
	"""
	
	homepage = "https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/#weights_for_data_instances"
	cran = "WeightSVM" 

	version("1.7-13", md5="da27d3a7f05d764695511928e678a4eb")

