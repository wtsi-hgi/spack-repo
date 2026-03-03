# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatelevelforest(RPackage):
	"""Historical State-Level Forest Cover Data in the United States

	Provides a unique dataset of historical forest cover across all states in the United States, spanning from 1907 to 2017, along with 1630 as a reference year. This dataset is important for understanding environmental changes and land use trends over time. It includes functionality for easy access of the data.
	"""
	
	cran = "StateLevelForest" 

	version("0.1.0", md5="f6a888c754249ef1e61730caf62c30bd")

	depends_on("r@2.10:", type=("build", "run"))
