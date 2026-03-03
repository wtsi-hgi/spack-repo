# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCatsim(RPackage):
	"""Binary and Categorical Image Similarity Index

	Computes a structural similarity metric (after the style of
    MS-SSIM for images) for binary and categorical 2D and 3D images. Can be
    based on accuracy (simple matching), Cohen's kappa, Rand index, adjusted
    Rand index, Jaccard index, Dice index, normalized mutual information, or
    adjusted mutual information. In addition, has fast computation
    of Cohen's kappa, the Rand indices, and the two mutual informations.
    Implements the methods of Thompson and Maitra (2020) <arXiv:2004.09073>.
	"""
	
	homepage = "https://github.com/gzt/catsim"
	cran = "catsim" 

	version("0.2.3", md5="dc7110eb62b440e9c3bf175bbcf95a3f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
