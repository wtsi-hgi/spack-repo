# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbcanalysis(RPackage):
	"""Computed ABC Analysis

	For a given data set, the package provides a novel method of computing precise limits to acquire subsets which are easily interpreted. Closely related to the Lorenz curve, the ABC curve visualizes the data by graphically representing the cumulative distribution function. Based on an ABC analysis the algorithm calculates, with the help of the ABC curve, the optimal limits by exploiting the mathematical properties pertaining to distribution of analyzed items. The data containing positive values is divided into three disjoint subsets A, B and C, with subset A comprising very profitable values, i.e. largest data values ("the important few"), subset B comprising values where the yield equals to the effort required to obtain it, and the subset C comprising of non-profitable values, i.e., the smallest data sets ("the trivial many"). Package is based on "Computed ABC Analysis for rational Selection of most informative Variables in multivariate Data", PLoS One. Ultsch. A., Lotsch J. (2015) <DOI:10.1371/journal.pone.0129767>.
	"""
	
	homepage = "https://www.uni-marburg.de/fb12/datenbionik/software-en"
	cran = "ABCanalysis" 

	version("1.2.1", md5="678e03837e25a922bf71bafe1f8de617")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
