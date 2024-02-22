# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCover2(RPackage):
	"""Process Digital Cover Photography Images of Tree Crowns

	Process Digital Cover Photography images of tree canopies to get canopy attributes like Foliage Cover and Leaf Area Index. 
    Detailed description of the methods in Chianucci et al. (2022) <doi:10.1007/s00468-018-1666-3>.
	"""
	
	cran = "coveR2" 

	version("1.0.0", md5="884f10b2182dcb0dfc8e4f32ede04bfc", url="https://cran.r-project.org/src/contrib/coveR2_1.0.0.tar.gz")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-autothresholdr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-mgc", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
