# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRelatedness(RPackage):
	"""Maximum Likelihood Estimation of Relatedness using EM Algorithm

	Inference of relatedness coefficients from a bi-allelic genotype matrix using a Maximum Likelihood estimation, Laporte, F., Charcosset, A. and Mary-Huard, T. (2017) <doi:10.1111/biom.12634>.
	"""
	
	cran = "Relatedness" 

	version("2.0", md5="3c2409cdf726c7215af3d432a1fd0839")

