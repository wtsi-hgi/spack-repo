# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLookuptable(RPackage):
	"""Look-Up Tables using S4

	Fits look-up tables by filling entries with the mean or median values of observations
            fall in partitions of the feature space. Partitions can be determined by user of the
            package using input argument feature.boundaries, and dimensions of the feature space
            can be any combination of continuous and categorical features provided by the data set.
            A Predict function directly fetches corresponding entry value, and a default value is
            defined as the mean or median of all available observations.
            The table and other components are represented using the S4 class lookupTable.
	"""
	
	cran = "lookupTable" 

	version("0.1", md5="7686f63cced179f5968ef62bd34745c5")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
