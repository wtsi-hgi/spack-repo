# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStfit(RPackage):
	"""Spatio-Temporal Functional Imputation Tool

	A general spatiotemporal satellite image imputation method based on sparse functional data analytic techniques. The imputation method applies and extends the Functional Principal Analysis by Conditional Estimation (PACE). The underlying idea for the proposed procedure is to impute a missing pixel by borrowing information from temporally and spatially contiguous pixels based on the best linear unbiased prediction.  
	"""
	
	cran = "stfit" 

	version("0.99.9", md5="5f8c6f119dfb9d0716f4860f10d180ba")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rastervis", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
