# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFilling(RPackage):
	"""Matrix Completion, Imputation, and Inpainting Methods

	Filling in the missing entries of a partially observed data is one of fundamental problems in various disciplines of mathematical science. For many cases, data at our interests have canonical form of matrix in that the problem is posed upon a matrix with missing values to fill in the entries under preset assumptions and models. We provide a collection of methods from multiple disciplines under Matrix Completion, Imputation, and Inpainting. See Davenport and Romberg (2016) <doi:10.1109/JSTSP.2016.2539100> for an overview of the topic.
	"""
	
	cran = "filling" 

	version("0.2.3", md5="37a996c2a5c978521ada74dd52f449e0")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-cvxr@1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-roptspace", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-nabor", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
