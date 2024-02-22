# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpader(RPackage):
	"""Species-Richness Prediction and Diversity Estimation with R

	Estimation of various biodiversity indices and related (dis)similarity measures based on individual-based (abundance) data or sampling-unit-based (incidence) data taken from one or multiple communities/assemblages.
	"""
	
	cran = "SpadeR" 

	version("0.1.1", md5="d02a468f7e355ee89371da92f4e1f35a")

	depends_on("r@2.14:", type=("build", "run"))
