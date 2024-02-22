# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComparemultiplemodels(RPackage):
	"""Finding the Best Model Using Eight Metrics Values

	In statistical modeling, multiple models need to be compared based on certain criteria. The method described here uses eight metrics from 'AllMetrics' package. ‘input_df’ is the data frame (at least two columns for comparison) containing metrics values in different rows of a column (which denotes a particular model’s performance). First five metrics are expected to be minimum and last three metrics are expected to be maximum for a model to be considered good. Firstly, every metric value (among first five) is searched in every columns and minimum values are denoted as ‘MIN’ and other values are denoted as ‘NA’. Secondly, every metric (among last three) is searched in every columns and maximum values are denoted as ‘MAX’ and other values are denoted as ‘NA’. ‘output_df’ contains the similar number of rows (which is 8) and columns (which is number of models to be compared) as of ‘input_df’. Values in ‘output_df’ are corresponding ‘NA’, ‘MIN’ or ‘MAX’. Finally, the column containing minimum number of ‘NA’ values is denoted as the best column. ‘min_NA_col’ gives the name of the best column (model). ‘min_NA_values’ are the corresponding metrics values. ‘BestColumn_metrics’ is the data frame (dimension: 1*8) containing different metrics of the best column (model). ‘best_column_results’ is the final result (a list) containing all of these output elements. In special case, if two columns having equal 'NA', it will be checked among these two column which one is having least 'NA' in first five rows and will be inferred as the best. More details about 'AllMetrics' can be found in Garai (2023) <doi:10.13140/RG.2.2.18688.30723>.
	"""
	
	cran = "CompareMultipleModels" 

	version("0.1.0", md5="f761661933924ba60a4bb2369ff7c7a8")

	depends_on("r-ceemdanml", type=("build", "run"))
