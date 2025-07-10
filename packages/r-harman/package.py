# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHarman(RPackage):
	"""The removal of batch effects from datasets using a PCA and constrained optimisation based technique

	Harman is a PCA and constrained optimisation based technique that maximises the removal of batch effects from datasets, with the constraint that the probability of overcorrection (i.e. removing genuine biological signal along with batch noise) is kept to a fraction which is set by the end-user.
	"""
	
	homepage = "http://www.bioinformatics.csiro.au/harman/"
	bioc = "Harman" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Harman_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Harman/Harman_1.30.0.tar.gz"]

	version("1.30.0", sha256="3750c9d1dff99a6e1bc89b0718f3f5116114e2598e06498744164f3c6b57d9cd")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ckmeans-1d-dp", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
