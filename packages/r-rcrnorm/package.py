# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcrnorm(RPackage):
	"""An Integrated Regression Model for Normalizing 'NanoString
nCounter' Data

	'NanoString nCounter' is a medium-throughput platform that measures gene or microRNA expression levels. Here is a publication that introduces this platform: Malkov (2009) <doi:10.1186/1756-0500-2-80>. Here is the webpage of 'NanoString nCounter' where you can find detailed information about this platform <https://www.nanostring.com/scientific-content/technology-overview/ncounter-technology>. It has great clinical application, such as diagnosis and prognosis of cancer. Implements integrated system of random-coefficient hierarchical regression model to normalize data from 'NanoString nCounter' platform so that noise from various sources can be removed.
	"""
	
	cran = "RCRnorm" 

	version("0.0.2", md5="4b5b74a84726bead59da5c034904f1a6")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
