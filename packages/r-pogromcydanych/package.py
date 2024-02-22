# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPogromcydanych(RPackage):
	"""DataCrunchers (PogromcyDanych) is the Massive Online Open Course
that Brings R and Statistics to the People

	The data sets used in the online course ,,PogromcyDanych''. You can process data in many ways. The course Data Crunchers will introduce you to this variety. For this reason we will work on datasets of different size (from several to several hundred thousand rows), with various level of complexity (from two to two thousand columns) and prepared in different formats (text data, quantitative data and qualitative data). All of these data sets were gathered in a single big package called PogromcyDanych to facilitate access to them. It contains all sorts of data sets such as data about offer prices of cars, results of opinion polls, information about changes in stock market indices, data about names given to newborn babies, ski jumping results or information about outcomes of breast cancer patients treatment.
	"""
	
	cran = "PogromcyDanych" 

	version("1.7.1", md5="0b246649c20b63d2d5b5a9dd181556bb")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-smarterpoland", type=("build", "run"))
