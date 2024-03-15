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

	version("1.30.0", md5="aaec4256c0cb2949d553ff81d94e48d2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ckmeans-1d-dp", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
