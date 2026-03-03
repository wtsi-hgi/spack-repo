# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFcm(RPackage):
	"""Inference of Fuzzy Cognitive Maps (FCMs)

	Provides a selection of 3 different inference rules (including additionally the clamped types of the referred inference rules) and 4 threshold functions in order to obtain the inference of the FCM (Fuzzy Cognitive Map). Moreover, the 'fcm' package returns a data frame of the concepts' values of each state after the inference procedure. Fuzzy cognitive maps were introduced by Kosko (1986) <doi:10.1002/int.4550010405> providing ideal causal cognition tools for modeling and simulating dynamic systems.
	"""
	
	cran = "fcm" 

	version("0.1.3", md5="6e745fd1dad9be428ecb595f63883eae")

	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
