# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScfa(RPackage):
	"""SCFA: Subtyping via Consensus Factor Analysis

	Subtyping via Consensus Factor Analysis (SCFA) can efficiently remove noisy signals from consistent molecular patterns in multi-omics data. SCFA first uses an autoencoder to select only important features and then repeatedly performs factor analysis to represent the data with different numbers of factors. Using these representations, it can reliably identify cancer subtypes and accurately predict risk scores of patients.
	"""
	
	homepage = "https://github.com/duct317/SCFA"
	bioc = "SCFA"

	version("1.18.0", commit="82dca55a37da09b23cec90e451ae17da88825bb6")
	version("1.12.0", commit="512730d1b35c34a54911299967c65d2a8ccd1cb7")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-torch@0.3:", type=("build", "run"))
	depends_on("r-coro", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rhpcblasctl", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
