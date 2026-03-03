# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REespca(RPackage):
	"""Eigenvectors from Eigenvalues Sparse Principal Component
Analysis (EESPCA)

	Contains logic for computing sparse principal components via the EESPCA method, 
    which is based on an approximation of the eigenvector/eigenvalue identity. 
    Includes logic to support execution of the TPower and rifle sparse PCA methods,
    as well as logic to estimate the sparsity parameters used by EESPCA, TPower and rifle
    via cross-validation to minimize the out-of-sample reconstruction error.
    H. Robert Frost (2021) <doi:10.1080/10618600.2021.1987254>.
	"""
	
	cran = "EESPCA" 

	version("0.7.0", md5="7b05531490d5d2dc7328f4e456661399")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rifle@1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pma", type=("build", "run"))
