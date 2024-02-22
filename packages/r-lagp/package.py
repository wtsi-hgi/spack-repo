# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLagp(RPackage):
	"""Local Approximate Gaussian Process Regression

	Performs approximate GP regression for large computer experiments and spatial datasets.  The approximation is based on finding small local designs for prediction (independently) at particular inputs. OpenMP and SNOW parallelization are supported for prediction over a vast out-of-sample testing set; GPU acceleration is also supported for an important subroutine.  OpenMP and GPU features may require special compilation.  An interface to lower-level (full) GP inference and prediction is provided. Wrapper routines for blackbox optimization under mixed equality and inequality constraints via an augmented Lagrangian scheme, and for large scale computer model calibration, are also provided.  For details and tutorial, see Gramacy (2016 <doi:10.18637/jss.v072.i01>.
	"""
	
	homepage = "https://bobby.gramacy.com/r_packages/laGP/"
	cran = "laGP" 

	version("1.5-9", md5="c5f10816e8b33f6da61b944ac98a03cb")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-tgp", type=("build", "run"))
