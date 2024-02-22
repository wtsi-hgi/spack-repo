# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeodiff(RPackage):
	"""Count model based differential expression and normalization on GeoMx RNA data

	A series of statistical models using count generating distributions for background modelling, feature and sample QC, normalization and differential expression analysis on GeoMx RNA data. The application of these methods are demonstrated by example data analysis vignette.
	"""
	
	homepage = "https://github.com/Nanostring-Biostats/GeoDiff"
	bioc = "GeoDiff" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/GeoDiff_1.8.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/GeoDiff/GeoDiff_1.8.0.tar.gz"]

	version("1.8.0", md5="f719fddf3486b6aad1f36ca439b55114")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-robust", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-geomxtools", type=("build", "run"))
	depends_on("r-nanostringnctools", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-roptim", type=("build", "run"))
