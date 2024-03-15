# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtensor2(RPackage):
	"""MultiLinear Algebra

	A set of tools for basic tensor operators.  A tensor in the context of data analysis in a multidimensional array. The tools in this package rely on using any discrete transformation (e.g. Fast Fourier Transform (FFT)).  Standard tools included are the Eigenvalue decomposition of a tensor, the QR decomposition and LU decomposition.  Other functionality includes the inverse of a tensor and the transpose of a symmetric tensor. Functionality in the package is outlined in Kernfeld et al. (2015) <https://www.sciencedirect.com/science/article/pii/S0024379515004358>.
	"""
	
	cran = "rTensor2" 

	version("0.2.0", md5="f8ffd2f4f71d46e5d333adbfcd8b472e", url="https://cran.r-project.org/src/contrib/rTensor2_0.2.0.tar.gz")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rtensor", type=("build", "run"))
	depends_on("r-wavethresh", type=("build", "run"))
	depends_on("r-gsignal", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
