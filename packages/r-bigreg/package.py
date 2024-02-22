# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigreg(RPackage):
	"""Generalized Linear Models (GLM) for Large Data Sets

	Allows the user to carry out GLM on very large
    data sets. Data can be created using the data_frame() function and appended
    to the object with object$append(data); data_frame and data_matrix objects
    are available that allow the user to store large data on disk. The data is
    stored as doubles in binary format and any character columns are transformed
    to factors and then stored as numeric (binary) data while a look-up table is
    stored in a separate .meta_data file in the same folder. The data is stored in
    blocks and GLM regression algorithm is modified and carries out a MapReduce-
    like algorithm to fit the model. The functions bglm(), and summary()
    and bglm_predict() are available for creating and post-processing of models.
    The library requires Armadillo installed on your system. It may not 
    function on windows since multi-core processing is done using mclapply() 
    which forks R on Unix/Linux type operating systems.
	"""
	
	cran = "bigReg" 

	version("0.1.5", md5="388c62ec2b25ba5d2d1b7f54557eaa94")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-uuid@0.1.2:", type=("build", "run"))
	depends_on("r-mass@7.3.39:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.5.200.1:", type=("build", "run"))
