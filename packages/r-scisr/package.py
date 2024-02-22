# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScisr(RPackage):
	"""Single-Cell Imputation using Subspace Regression

	Provides an imputation pipeline for single-cell RNA sequencing data. 
  The 'scISR' method uses a hypothesis-testing technique to identify zero-valued entries that are most likely affected by dropout events and estimates the dropout values using a subspace regression model (Tran et.al. (2022) <DOI:10.1038/s41598-022-06500-4>).
	"""
	
	homepage = "https://github.com/duct317/scISR"
	cran = "scISR" 

	version("0.1.1", md5="5667b5dc9b37061c6fdd4ab524164450")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-entropy", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-pinsplus", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
