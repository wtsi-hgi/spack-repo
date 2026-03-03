# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMindonstats(RPackage):
	"""Data sets included in Utts and Heckard's Mind on Statistics

	66 data sets that were imported using read.table() where appropriate but more commonly after converting to a csv file for importing via read.csv().
	"""
	
	cran = "MindOnStats" 

	version("0.11", md5="9bd4188808198984d7e948ed78492997")

	depends_on("r@2.14:", type=("build", "run"))
