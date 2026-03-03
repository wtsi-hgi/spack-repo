# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChronosphere(RPackage):
	"""Evolving Earth System Variables

	The implemented functions allow the query, download, and import of remotely-stored and version-controlled data items. The inherent meta-database maps data files and import code to programming classes and allows access to these items via files deposited in public repositories. The purpose of the project is to increase reproducibility and establish version tracking of results from (paleo)environmental/ecological research.
	"""
	
	cran = "chronosphere" 

	version("0.6.1", md5="ffa92c23409944d8eb1dfaf8f2a9364c")

	depends_on("r@3.5:", type=("build", "run"))
