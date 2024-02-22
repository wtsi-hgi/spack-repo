# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImputelcmd(RPackage):
	"""A Collection of Methods for Left-Censored Missing Data
Imputation

	A collection of functions for left-censored missing data imputation. Left-censoring is a special case of missing not at random (MNAR)  mechanism that generates non-responses in proteomics experiments. The package also contains functions to artificially generate peptide/protein expression data (log-transformed) as random draws from a multivariate Gaussian distribution as well as a function to generate missing data (both randomly and non-randomly). For comparison reasons, the package also contains several wrapper functions for the imputation of non-responses that are missing at random. * New functionality has been added: a hybrid method that allows the imputation of missing values in a more complex scenario where the missing data are both MAR and MNAR.
	"""
	
	cran = "imputeLCMD" 

	version("2.1", md5="f6f43f17c8267a51f384da696189e549")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tmvtnorm", type=("build", "run"))
	depends_on("r-norm", type=("build", "run"))
	depends_on("r-pcamethods", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
