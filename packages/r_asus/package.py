# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsus(RPackage):
	"""Adaptive SURE Thresholding Using Side Information

	Provides the ASUS procedure for estimating a high dimensional sparse parameter in the presence of auxiliary data that encode side information on sparsity. It is a robust data combination procedure in the sense that even when pooling non-informative auxiliary data ASUS would be at least as efficient as competing soft thresholding based methods that do not use auxiliary data. 
    For more information, please see the paper Adaptive Sparse Estimation with Side Information by Banerjee, Mukherjee and Sun (JASA 2020).
	"""
	
	homepage = "https://github.com/trambakbanerjee/asus#asus"
	cran = "asus" 

	version("1.5.0", md5="b750e2668b5e5dcd24cfa6052a940d23")

	depends_on("r-wavethresh", type=("build", "run"))
