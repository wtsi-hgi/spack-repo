# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBcv(RPackage):
	"""Cross-Validation for the SVD (Bi-Cross-Validation)

	
    Methods for choosing the rank of an SVD (singular value decomposition) 
    approximation via cross validation. The package provides both Gabriel-style 
    "block" holdouts and Wold-style "speckled" holdouts. It also includes an 
    implementation of the SVDImpute algorithm. For more information about
    Bi-cross-validation, see Owen & Perry's 2009 AoAS article
    (at <arXiv:0908.2062>) and Perry's 2009 PhD thesis
    (at <arXiv:0909.3052>).
	"""
	
	homepage = "https://github.com/michbur/bcv"
	cran = "bcv" 

	version("1.0.2", md5="06b9609e2a068f4adb4ab47228df69a6")

