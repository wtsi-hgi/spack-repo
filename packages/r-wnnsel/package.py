# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWnnsel(RPackage):
	"""Weighted Nearest Neighbor Imputation of Missing Values using
Selected Variables

	New tools for the imputation of missing values in high-dimensional
    data are introduced using the non-parametric nearest neighbor methods. It
    includes weighted nearest neighbor imputation methods that use specific
    distances for selected variables. It includes an automatic procedure of cross
    validation and does not require prespecified values of the tuning parameters.
    It can be used to impute missing values in high-dimensional data when the sample
    size is smaller than the number of predictors. For more information see Faisal
    and Tutz (2017) <doi:10.1515/sagmb-2015-0098>.
	"""
	
	cran = "wNNSel" 

	version("0.1", md5="423c0f56961d3c42e66ddff055641d83")

