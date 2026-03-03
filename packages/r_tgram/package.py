# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTgram(RPackage):
	"""Compute and Plot Tracheidograms

	Functions to compute and plot tracheidograms, as in De Soto et al. (2011) <doi:10.1139/x11-045>.
	"""
	
	cran = "tgram" 

	version("0.2-3", md5="3d86800882206f8abd5c78c5c6621e1a")

	depends_on("r-zoo", type=("build", "run"))
