# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFaseg(RPackage):
	"""Joint Segmentation of Correlated Time Series

	It contains a function designed to the joint segmentation in the mean of several correlated series. The method is described in the paper X. Collilieux, E. Lebarbier and S. Robin. A factor model approach for the joint segmentation with between-series correlation (2015) <arXiv:1505.05660>.
	"""
	
	cran = "FASeg" 

	version("0.1.9", md5="ee3ea108a86a49d83a8ec9c3982a5089")

	depends_on("r@2.10:", type=("build", "run"))
