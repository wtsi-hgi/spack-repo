# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPanelpomp(RPackage):
	"""Inference for Panel Partially Observed Markov Processes

	Data analysis based on panel partially-observed Markov process (PanelPOMP) models. To implement such models, simulate them and fit them to panel data, 'panelPomp' extends some of the facilities provided for time series data by the 'pomp' package. Implemented methods include filtering (panel particle filtering) and maximum likelihood estimation (Panel Iterated Filtering) as proposed in Breto, Ionides and King (2020) "Panel Data Analysis via Mechanistic Models" <doi:10.1080/01621459.2019.1604367>.
	"""
	
	cran = "panelPomp" 

	version("1.1", md5="f6c4223326fc53b3442fef04d64f425f")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-pomp@4.5.2:", type=("build", "run"))
