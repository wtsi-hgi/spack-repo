# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimedf(RPackage):
	"""Subset and Flag Data Frames with Times by the Use of Periods

	Data frames with time information are subset and flagged with period information. Data frames with times are dealt as timeDF objects and periods are represented as periodDF objects.
	"""
	
	homepage = "https://github.com/niceume/timeDF"
	cran = "timeDF" 

	version("0.9.0", md5="2919ce27674f366b833f5bc244e59166")

	depends_on("r-rcpp", type=("build", "run"))
