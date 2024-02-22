# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCsdata(RPackage):
	"""Structural Data for Norway

	Datasets relating to population in municipalities, municipality/county matching, and how different municipalities have merged/redistricted over time from 2006 to 2024.
	"""
	
	homepage = "https://www.csids.no/csdata/"
	cran = "csdata" 

	version("2024.1.17", md5="5e4d644f39307641ab7a315a04029311")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
