# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTensorregress(RPackage):
	"""Supervised Tensor Decomposition with Side Information

	Implement the alternating algorithm for supervised tensor decomposition with interactive side information. Details can be found in the publication Hu, Jiaxin, Chanwoo Lee, and Miaoyan Wang. "Generalized Tensor Decomposition with features on multiple modes." Journal of Computational and Graphical Statistics, Vol. 31, No. 1, 204-218, 2022 <doi:10.1080/10618600.2021.1978471>.
	"""
	
	cran = "tensorregress" 

	version("5.1", md5="93c7f2b91601c44007e5ac457a76d8e7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
