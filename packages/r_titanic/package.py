# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTitanic(RPackage):
	"""Titanic Passenger Survival Data Set

	This data set provides information on the fate of passengers on
    the fatal maiden voyage of the ocean liner "Titanic", summarized according
    to economic status (class), sex, age and survival. Whereas the base R
    Titanic data found by calling data("Titanic") is an array resulting from
    cross-tabulating 2201 observations, these data sets are the individual
    non-aggregated observations and formatted in a machine learning context
    with a training sample, a testing sample, and two additional data sets
    that can be used for deeper machine learning analysis. These data sets
    are also the data sets downloaded from the Kaggle competition and thus
    lowers the barrier to entry for users new to R or machine learing.
	"""
	
	homepage = "https://github.com/paulhendricks/titanic"
	cran = "titanic" 

	version("0.1.0", md5="0c9110b21b4c9e1156ce73ebbedc2c33")

	depends_on("r@3.1.2:", type=("build", "run"))
