# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGfe(RPackage):
	"""Gross Flows Estimation under Complex Surveys

	The philosophy in the package is described in Stasny (1988) <doi:10.2307/1391558> and Gutierrez, A., Trujillo, L. & Silva, N. (2014), <ISSN:1492-0921> to estimate the gross flows under complex surveys using a Markov chain approach with non response.
	"""
	
	cran = "GFE" 

	version("0.1.1", md5="7f921ba544a943cc630f47afdf9d29af")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-teachingsampling", type=("build", "run"))
