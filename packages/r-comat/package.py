# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComat(RPackage):
	"""Creates Co-Occurrence Matrices of Spatial Data

	Builds co-occurrence matrices based on spatial raster data.
    It includes creation of weighted co-occurrence matrices (wecoma) and 
    integrated co-occurrence matrices 
    (incoma; Vadivel et al. (2007) <doi:10.1016/j.patrec.2007.01.004>).
	"""
	
	homepage = "https://jakubnowosad.com/comat/"
	cran = "comat" 

	version("0.9.5", md5="d2f9cb862953303a368e8db6d15ae4c4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
