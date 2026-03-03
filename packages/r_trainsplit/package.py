# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrainsplit(RPackage):
	"""Split a Dataframe, Tibble, or Data.table into Training and Test
Sets

	Split a dataframe, tibble, or data.table into a list containing training and test sets. Can specify either number or percentage of observations to go into the training set.
	"""
	
	homepage = "https://github.com/eastnile/trainsplit"
	cran = "trainsplit" 

	version("1.0", md5="761191f93515a93a903156e754e9c2c6")

	depends_on("r-data-table", type=("build", "run"))
