# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHiclimr(RPackage):
	"""Hierarchical Climate Regionalization

	A tool for Hierarchical Climate Regionalization applicable to any correlation-based clustering.
             It adds several features and a new clustering method (called, 'regional' linkage) to hierarchical
             clustering in R ('hclust' function in 'stats' library): data regridding, coarsening spatial resolution,
             geographic masking, contiguity-constrained clustering, data filtering by mean and/or variance
             thresholds, data preprocessing (detrending, standardization, and PCA), faster correlation function
             with preliminary big data support, different clustering methods, hybrid hierarchical clustering,
             multivariate clustering (MVC), cluster validation, visualization of regionalization results, and
             exporting region map and mean timeseries into NetCDF-4 file.
             The technical details are described in Badr et al. (2015) <doi:10.1007/s12145-015-0221-7>.
	"""
	
	homepage = "https://hsbadr.github.io/HiClimR/"
	cran = "HiClimR" 

	version("2.2.1", md5="7aade3ca16cc869993bce23caea5654f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("netcdf-c@4.1:", type=("build", "link", "run"))
