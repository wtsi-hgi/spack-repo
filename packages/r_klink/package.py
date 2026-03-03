# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKlink(RPackage):
	"""Kinship Analysis with Linked Markers

	A 'shiny' application for forensic kinship testing, based on
    the 'pedsuite' R packages. 'KLINK' is closely aligned with the (non-R)
    software 'Familias' and 'FamLink', but offers several unique features,
    including visualisations and automated report generation. The
    calculation of likelihood ratios supports pairs of linked markers, and
    all common mutation models.
	"""
	
	homepage = "https://github.com/magnusdv/KLINK"
	cran = "KLINK" 

	version("0.7.2", md5="d8c1b511b4104fd32a4d93a9d62a3c86")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-forrel@1.6:", type=("build", "run"))
	depends_on("r-gt@0.9:", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-pedfamilias", type=("build", "run"))
	depends_on("r-pedmut@0.7.1:", type=("build", "run"))
	depends_on("r-pedprobr@0.8:", type=("build", "run"))
	depends_on("r-pedtools@2.5:", type=("build", "run"))
	depends_on("r-shiny@1.7.4:", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-verbalisr", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
