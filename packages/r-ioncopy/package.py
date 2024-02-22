# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIoncopy(RPackage):
	"""Calling Copy Number Alterations in Amplicon Sequencing Data

	Method for the calculation of copy numbers and calling of copy number alterations. The algorithm uses coverage data from amplicon sequencing of a sample cohort as input. The method includes significance assessment, correction for multiple testing and does not depend on normal DNA controls. Budczies (2016 Mar 15) <doi:10.18632/oncotarget.7451>.
	"""
	
	cran = "ioncopy" 

	version("2.2.2", md5="053139d01cd2cc13a76a1637b51c396e")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
