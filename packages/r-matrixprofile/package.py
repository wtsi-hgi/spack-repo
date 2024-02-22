# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatrixprofile(RPackage):
	"""Matrix Profile

	A simple and the early stage package for matrix profile based on the paper of Chin-Chia Michael Yeh, Yan Zhu, Liudmila Ulanova, Nurjahan Begum, Yifei Ding, Hoang Anh Dau, Diego Furtado Silva, Abdullah Mueen, and Eamonn Keogh (2016) <DOI:10.1109/ICDM.2016.0179>. This package calculates all-pairs-similarity for a given window size for time series data.
	"""
	
	homepage = "https://github.com/ainsuotain/matrixprofile"
	cran = "matrixProfile" 

	version("0.5.0", md5="0d37bfa120a23787e1341d44f97c4ea5")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ttr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-fftw", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
