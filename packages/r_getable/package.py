# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGetable(RPackage):
	"""Fetching Tabular Data "Onload" in Compiled R Markdown HTML
Documents

	Dynamically retrieve data from the web to render HTML tables
    on inspection in R Markdown HTML documents.
	"""
	
	homepage = "https://yongfu.name/getable/"
	cran = "getable" 

	version("1.0.3", md5="cbb639fb96727c7f3864823a3219762a")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
