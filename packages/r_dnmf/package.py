# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDnmf(RPackage):
	"""Discriminant Non-Negative Matrix Factorization

	Discriminant Non-Negative Matrix Factorization aims to extend the Non-negative Matrix Factorization algorithm in order to extract features that enforce not only the spatial locality, but also the separability between classes in a discriminant manner. It refers to three article, Zafeiriou, Stefanos, et al. "Exploiting discriminant information in nonnegative matrix factorization with application to frontal face verification." Neural Networks, IEEE Transactions on 17.3 (2006): 683-695. Kim, Bo-Kyeong, and Soo-Young Lee. "Spectral Feature Extraction Using dNMF for Emotion Recognition in Vowel Sounds." Neural Information Processing. Springer Berlin Heidelberg, 2013. and Lee, Soo-Young, Hyun-Ah Song, and Shun-ichi Amari. "A new discriminant NMF algorithm and its application to the extraction of subtle emotional differences in speech." Cognitive neurodynamics 6.6 (2012): 525-535.
	"""
	
	homepage = "https://github.com/zhilongjia/DNMF"
	cran = "DNMF" 

	version("1.4.2", md5="d5ab23bf78bc0d8800bfdb40371694c3")

	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
