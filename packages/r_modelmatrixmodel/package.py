# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModelmatrixmodel(RPackage):
	"""Create Model Matrix and Save the Transforming Parameters

	The model.matrix() function in R is  convenient for transforming training dataset for modeling. 
    But it does not save any parameter used in transformation, so it is hard to apply the same transformation 
    to test dataset or new dataset. This package is created to solve the problem.
	"""
	
	cran = "ModelMatrixModel" 

	version("0.1.0", md5="5bdb2230259d9f97edb7bb2475de3dfe")

	depends_on("r-matrix", type=("build", "run"))
