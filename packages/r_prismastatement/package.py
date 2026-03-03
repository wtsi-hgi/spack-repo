# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrismastatement(RPackage):
	"""Plot Flow Charts According to the "PRISMA" Statement

	Plot a PRISMA <http://prisma-statement.org/> flow
    chart describing the identification, screening, eligibility and
    inclusion or studies in systematic reviews. The PRISMA statement
    defines an evidence-based, minimal set of items for reporting in
    systematic reviews and meta-analyses. PRISMA should be used for the
    reporting of studies evaluating randomized clinical trials (RCT), and
    is also for reporting on systematic reviews of other types of
    research. There is also a function to generate flow charts describing
    exclusions and inclusions for any kind of study.
	"""
	
	homepage = "https://github.com/jackwasey/PRISMAstatement"
	cran = "PRISMAstatement" 

	version("1.1.1", md5="8bc601a80ca2054302791e1b2fe21ffa")

	depends_on("r-diagrammer", type=("build", "run"))
