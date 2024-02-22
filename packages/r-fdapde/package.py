# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdapde(RPackage):
	"""Physics-Informed Spatial and Functional Data Analysis

	An implementation of regression models with partial differential regularizations, making use of the Finite Element Method. The models efficiently handle data distributed over irregularly shaped domains and can comply with various conditions at the boundaries of the domain. A priori information about the spatial structure of the phenomenon under study can be incorporated in the model via the differential regularization. See Sangalli, L. M. (2021) <doi:10.1111/insr.12444> "Spatial Regression With Partial Differential Equation Regularisation" for an overview. The release 1.1-9 requires R (>= 4.2.0) to be installed on windows machines.
	"""
	
	cran = "fdaPDE" 

	version("1.1-17", md5="a26077f90bfca2b4e5c4e9f43e454b2d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
