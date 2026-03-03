# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAuc(RPackage):
	"""Threshold Independent Performance Measures for Probabilistic
Classifiers

	Various functions to compute the area under the curve of selected measures: The area under the sensitivity curve (AUSEC), the area under the specificity curve (AUSPC), the area under the accuracy curve (AUACC), and the area under the receiver operating characteristic curve (AUROC). Support for visualization and partial areas is included.
	"""
	
	cran = "AUC" 

	version("0.3.2", md5="4a1e66f9889fc2fe02c734e1e1fd063f")

