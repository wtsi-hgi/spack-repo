# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpringer(RPackage):
	"""Sparse Group Variable Selection for Gene-Environment
Interactions in the Longitudinal Study

	Recently, regularized variable selection has emerged as a powerful tool to identify and dissect gene-environment interactions. Nevertheless, in longitudinal studies with high dimensional genetic factors, regularization methods for G×E interactions have not been systematically developed. In this package, we provide the implementation of sparse group variable selection, based on both the quadratic inference function (QIF) and generalized estimating equation (GEE), to accommodate the bi-level selection for longitudinal G×E studies with high dimensional genomic features. Alternative methods conducting only the group or individual level selection have also been included. The core modules of the package have been developed in C++. 
	"""
	
	homepage = "https://github.com/feizhoustat/springer"
	cran = "springer" 

	version("0.1.9", md5="800a52a051a4f47f6bbd8715e041586f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
