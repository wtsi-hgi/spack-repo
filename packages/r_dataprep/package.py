# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDataprep(RPackage):
	"""Efficient and Flexible Data Preprocessing Tools

	Efficiently and flexibly preprocess data using a set of data filtering, deletion, and interpolation tools.
    These data preprocessing methods are developed based on the principles of completeness, accuracy, threshold method, and linear interpolation and through the setting of constraint conditions, time completion & recovery, and fast & efficient calculation and grouping.
    Key preprocessing steps include deletions of variables and observations, outlier removal, and missing values (NA) interpolation, which are dependent on the incomplete and dispersed degrees of raw data.
    They clean data more accurately, keep more samples, and add no outliers after interpolation, compared with ordinary methods.
    Auto-identification of consecutive NA via run-length based grouping is used in observation deletion, outlier removal, and NA interpolation;
    thus, new outliers are not generated in interpolation. Conditional extremum is proposed to realize point-by-point weighed outlier removal that saves non-outliers from being removed.
    Plus, time series interpolation with values to refer to within short periods further ensures reliable interpolation.
    These methods are based on and improved from the reference: Liang, C.-S., Wu, H., Li, H.-Y., Zhang, Q., Li, Z. & He, K.-B. (2020) <doi:10.1016/j.scitotenv.2020.140923>.
	"""
	
	cran = "dataprep" 

	version("0.1.5", md5="272d14ed42b665f3ca24259bb280c997")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
