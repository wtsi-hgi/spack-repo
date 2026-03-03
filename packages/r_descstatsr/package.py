# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDescstatsr(RPackage):
	"""Descriptive Univariate Statistics

	It generates summary statistics on the input dataset using different descriptive univariate 
    statistical measures on entire data or at a group level. Though there are other packages which does 
    similar job but each of these are deficient in one form or other, in the measures generated, in
    treating numeric, character and date variables alike, no functionality to view these measures on a
    group level or the way the output is represented. Given the foremost role of the descriptive statistics
    in any of the exploratory data analysis or solution development, there is a need for a more constructive, 
    structured and refined version over these packages. This is the idea behind the package and it brings 
    together all the required descriptive measures to give an initial understanding of the data quality, 
    distribution in a faster,easier and elaborative way.The function brings an additional capability to be 
    able to generate these statistical measures on the entire dataset or at a group level. It calculates measures 
    of central tendency (mean, median), distribution (count, proportion), dispersion (min, max, quantile, 
    standard deviation, variance) and shape (skewness, kurtosis). Addition to these measures, it provides information on 
    the data type, count on no. of rows, unique entries and percentage of missing entries. More importantly the measures 
    are generated based on the data types as required by them,rather than applying numerical measures on character and 
    data variables and vice versa. Output as a dataframe object gives a very neat representation, which often is useful 
    when working with a large number of columns. It can easily be exported as csv and analyzed further or presented as a 
    summary report for the data.
	"""
	
	cran = "descstatsr" 

	version("0.1.0", md5="10d6a83f2f4c8271b9c6da94e741d000")

	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
