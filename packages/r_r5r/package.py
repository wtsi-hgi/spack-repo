# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR5r(RPackage):
	"""Rapid Realistic Routing with 'R5'

	Rapid realistic routing on multimodal transport networks
    (walk, bike, public transport and car) using 'R5', the Rapid Realistic
    Routing on Real-world and Reimagined networks engine
    <https://github.com/conveyal/r5>. The package allows users to generate
    detailed routing analysis or calculate travel time matrices using
    seamless parallel computing on top of the R5 Java machine.  While R5
    is developed by Conveyal, the package r5r is independently developed
    by a team at the Institute for Applied Economic Research (Ipea) with
    contributions from collaborators. Apart from the documentation in this
    package, users will find additional information on R5 documentation at
    <https://docs.conveyal.com/>. Although we try to keep new releases of
    r5r in synchrony with R5, the development of R5 follows Conveyal's
    independent update process. Hence, users should confirm the R5 version
    implied by the Conveyal user manual (see
    <https://docs.conveyal.com/changelog>) corresponds with the R5 version
    that r5r depends on.
	"""
	
	homepage = "https://github.com/ipeaGIT/r5r"
	cran = "r5r" 

	version("1.1.0", md5="58a8e66b804bfd0135da373fb3d88018")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-concaveman", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rjava@0.9.10:", type=("build", "run"))
	depends_on("r-sf@1.0.12:", type=("build", "run"))
	depends_on("r-sfheaders", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
	depends_on("openjdk@11.0:", type=("build", "link", "run"))
