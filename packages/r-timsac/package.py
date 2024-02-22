# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimsac(RPackage):
	"""Time Series Analysis and Control Package

	Functions for statistical analysis, prediction and control of time
 series based mainly on Akaike and Nakagawa (1988) <ISBN 978-90-277-2786-2>.
	"""
	
	cran = "timsac" 

	version("1.3.8-4", md5="e325a5e8bceab47722a95d487c6a8f06")

	depends_on("r@4:", type=("build", "run"))
