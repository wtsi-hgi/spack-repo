# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPreregr(RPackage):
	"""Specify (Pre)Registrations and Export Them Human- And
Machine-Readably

	Preregistrations, or more generally, registrations, enable
    explicit timestamped and (often but not necessarily publicly) frozen
    documentation of plans and expectations as well as decisions and
    justifications. In research, preregistrations are commonly used to
    clearly document plans and facilitate justifications of deviations from
    those plans, as well as decreasing the effects of publication bias by
    enabling identification of research that was conducted but not published.
    Like reporting guidelines, (pre)registration forms often have specific
    structures that facilitate systematic reporting of important items. The
    'preregr' package facilitates specifying (pre)registrations in R and
    exporting them to a human-readable format (using R Markdown partials or
    exporting to an 'HTML' file) as well as human-readable embedded data
    (using 'JSON'), as well as importing such exported (pre)registration
    specifications from such embedded 'JSON'.
	"""
	
	homepage = "https://preregr.opens.science"
	cran = "preregr" 

	version("0.2.9", md5="9c4463c9b1b0dd29aff5b72774a930ef")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cli@3:", type=("build", "run"))
	depends_on("r-jsonlite@1.7:", type=("build", "run"))
	depends_on("r-rmdpartials@0.5.8:", type=("build", "run"))
	depends_on("r-yaml@2.2:", type=("build", "run"))
