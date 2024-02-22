# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlockmatrix(RPackage):
	"""blockmatrix: Tools to solve algebraic systems with partitioned
matrices

	Some elementary matrix algebra tools are implemented to manage
    block matrices or partitioned matrix, i.e. "matrix of matrices"
    (http://en.wikipedia.org/wiki/Block_matrix). The block matrix is here
    defined as a new S3 object. In this package, some methods for "matrix"
    object are rewritten for "blockmatrix" object. New methods are implemented.
    This package was created to solve equation systems with block matrices for
    the analysis of environmental vector time series .
    Bugs/comments/questions/collaboration of any kind are warmly welcomed.
	"""
	
	homepage = "http://cri.gmpf.eu/Research/Sustainable-Agro-Ecosystems-and-Bioresources/Dynamics-in-the-agro-ecosystems/people/Emanuele-Cordano"
	cran = "blockmatrix" 

	version("1.0", md5="274119de1e0dabbfff8b884c670f3b5f")

	depends_on("r@2.13:", type=("build", "run"))
