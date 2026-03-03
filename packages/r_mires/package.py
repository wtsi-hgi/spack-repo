# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMires(RPackage):
	"""Measurement Invariance Assessment Using Random Effects Models
and Shrinkage

	Estimates random effect latent measurement models, wherein the loadings, residual variances, intercepts, latent means, and latent variances all vary across groups. The random effect variances of the measurement parameters are then modeled using a hierarchical inclusion model, wherein the inclusion of the variances (i.e., whether it is effectively zero or non-zero) is informed by similar parameters (of the same type, or of the same item). This additional hierarchical structure allows the evidence in favor of partial invariance to accumulate more quickly, and yields more certain decisions about measurement invariance. Martin, Williams, and Rast (2020) <doi:10.31234/osf.io/qbdjt>.
	"""
	
	cran = "MIRES" 

	version("0.1.0", md5="9c46c9bf84a1235630e38d1fa5822db4")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rstantools@2:", type=("build", "run"))
	depends_on("r-formula@1.2.1:", type=("build", "run"))
	depends_on("r-mvtnorm@1:", type=("build", "run"))
	depends_on("r-dirichletprocess@0.4:", type=("build", "run"))
	depends_on("r-truncnorm@1:", type=("build", "run"))
	depends_on("r-pracma@2.2.9:", type=("build", "run"))
	depends_on("r-cubature@2:", type=("build", "run"))
	depends_on("r-logspline@2.1:", type=("build", "run"))
	depends_on("r-nlme@3.1:", type=("build", "run"))
	depends_on("r-hdinterval@0.2.2:", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
