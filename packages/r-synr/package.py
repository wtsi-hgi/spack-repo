# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSynr(RPackage):
	"""Explore and Process Synesthesia Consistency Test Data

	Explore synesthesia
  consistency test data, calculate consistency scores, 
  and classify participant data as valid or invalid.
	"""
	
	homepage = "https://datalowe.github.io/synr/"
	cran = "synr" 

	version("1.0.0", md5="3610da3446b55ea47c68b7a82106f602")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-data-table@1.12:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-dbscan@1.1:", type=("build", "run"))
