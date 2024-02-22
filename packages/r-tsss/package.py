# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsss(RPackage):
	"""Time Series Analysis with State Space Model

	Functions for statistical analysis, modeling and simulation of time
 series with state space model, based on the methodology in Kitagawa
 (2020, ISBN: 978-0-367-18733-0).
	"""
	
	cran = "TSSS" 

	version("1.3.4-5", md5="2877e20d8977398a6006d1cb1a9646c6")

	depends_on("r@3.6:", type=("build", "run"))
