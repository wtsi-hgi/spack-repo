# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatrixprofiler(RPackage):
	"""Matrix Profile for R

	This is the core functions needed by the 'tsmp' package.  The
    low level and carefully checked mathematical functions are here.
    These are implementations of the Matrix Profile concept that was
    created by CS-UCR <http://www.cs.ucr.edu/~eamonn/MatrixProfile.html>.
	"""
	
	homepage = "https://github.com/matrix-profile-foundation/matrixprofiler"
	cran = "matrixprofiler" 

	version("0.1.9", md5="518d63b483a0e850dbc9f8226124c153")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-checkmate@2.1:", type=("build", "run"))
	depends_on("r-rcpp@1.0.9:", type=("build", "run"))
	depends_on("r-rcppparallel@5.1.5:", type=("build", "run"))
	depends_on("r-rcppprogress@0.4.2:", type=("build", "run"))
	depends_on("r-rcppthread@2.1.3:", type=("build", "run"))
