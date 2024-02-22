# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHarvestTree(RPackage):
	"""Harvest the Classification Tree

	Aimed at applying the Harvest classification tree algorithm, modified algorithm of classic classification tree.The harvested tree has advantage of deleting redundant rules in trees, leading to a simplify and more efficient tree model.It was firstly used in drug discovery field, but it also performs well in other kinds of data, especially when the region of a class is disconnected. This package also improves the basic harvest classification tree algorithm by extending the field of data of algorithm to both continuous and categorical variables. To learn more about the harvest classification tree algorithm, you can go to http://www.stat.ubc.ca/Research/TechReports/techreports/220.pdf for more information. 
	"""
	
	cran = "Harvest.Tree" 

	version("1.1", md5="8fa24c2ab02c314abaab1cfeb74ff315")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
