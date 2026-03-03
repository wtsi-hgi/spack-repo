# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsmp(RPackage):
	"""Time Series with Matrix Profile

	A toolkit implementing the Matrix Profile concept
    that was created by CS-UCR
    <http://www.cs.ucr.edu/~eamonn/MatrixProfile.html>.
	"""
	
	homepage = "https://github.com/matrix-profile-foundation/tsmp"
	cran = "tsmp" 

	version("0.4.15", md5="58cd25f1b2f4559f881ca5b983086b06")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-audio", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rcpp@1.0.3:", type=("build", "run"))
	depends_on("r-rcppparallel@5:", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
