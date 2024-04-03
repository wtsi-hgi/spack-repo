# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpltr(RPackage):
	"""Generalized Partially Linear Tree-Based Regression Model

	Combining a generalized linear model with an additional tree part 
          on the same scale. A four-step procedure is proposed to fit the model and test 
          the joint effect of the selected tree part while adjusting on confounding factors. 
          We also proposed an ensemble procedure based on the bagging to improve prediction 
          accuracy and computed several scores of importance for variable selection.
          See 'Cyprien Mbogning et al.'(2014)<doi:10.1186/2043-9113-4-6> and 
         'Cyprien Mbogning et al.'(2015)<doi:10.1159/000380850> 
          for an overview of all the methods implemented in this package.
	"""
	
	cran = "GPLTR" 

	version("1.5", md5="39cca512a2b52196ea83dc47f9a4c7a9")

	depends_on("r-rpart", type=("build", "run"))
