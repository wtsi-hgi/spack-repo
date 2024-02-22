# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKergp(RPackage):
	"""Gaussian Process Laboratory

	Gaussian process regression with an emphasis on kernels.
    Quantitative and qualitative inputs are accepted. Some pre-defined
    kernels are available, such as radial or tensor-sum for
    quantitative inputs, and compound symmetry, low rank, group kernel
    for qualitative inputs. The user can define new kernels and
    composite kernels through a formula mechanism. Useful methods
    include parameter estimation by maximum likelihood, simulation,
    prediction and leave-one-out validation.
	"""
	
	cran = "kergp" 

	version("0.5.7", md5="5e9eebb28ae601b034f75c52f53131ad")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dofuture", type=("build", "run"))
