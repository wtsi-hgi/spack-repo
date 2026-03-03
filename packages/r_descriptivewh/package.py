# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDescriptivewh(RPackage):
	"""Descriptive Statistics

	Exploratory analysis of a data base. Using the functions of this package is possible to filter the data set detecting atypical values (outliers) and to perform exploratory analysis through visual inspection or dispersion measures. With this package you can explore the structure of your data using several parameters at the same time joining statistical parameters with different graphics. Finally, this package aid to confirm or reject the hypothesis that your data structure presents a normal distribution. Therefore this package is useful to get a previous insight of your data before to carry out statistical analysis.
	"""
	
	homepage = "https://github.com/William-HC/DescriptiveWH"
	cran = "DescriptiveWH" 

	version("1.0.3", md5="664eb04979a3da498440f82da66b929f")

	depends_on("r@3.6:", type=("build", "run"))
