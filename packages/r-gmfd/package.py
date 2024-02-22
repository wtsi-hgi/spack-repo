# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmfd(RPackage):
	"""Inference and Clustering of Functional Data

	Some methods for the inference and clustering of univariate and 
             multivariate functional data, using a generalization of Mahalanobis
             distance, along with some functions useful for the analysis of functional data.
             For further details, see Martino A., Ghiglietti, A., Ieva, F. and Paganoni A. M. (2017) <arXiv:1708.00386>.
	"""
	
	cran = "gmfd" 

	version("1.0.1", md5="6160e3392b3af9ea2188862299bf8afd")

	depends_on("r@3.3:", type=("build", "run"))
