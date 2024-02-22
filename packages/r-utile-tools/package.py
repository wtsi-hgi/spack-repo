# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUtileTools(RPackage):
	"""Summarize Data for Publication

	Tools for formatting and summarizing data for outcomes research.
	"""
	
	homepage = "https://efinite.github.io/utile.tools/"
	cran = "utile.tools" 

	version("0.3.0", md5="f5b9a1bcbd4458de91c70c356ab6109f")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
