# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRreg(RPackage):
	"""Visualization for Norwegian Health Quality Registries

	Assists for presentation and visualization of data from the Norwegian Health Quality Registries following the standardization based on the requirement specified by the National Service for Health Quality Registries. This requirement can be accessed from (<https://www.kvalitetsregistre.no/resultater-til-publisering-pa-nett>). Unfortunately the website is only available in Norwegian.
	"""
	
	cran = "rreg" 

	version("0.2.1", md5="72e072d5cb285a814085cc2448217b96")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-directlabels", type=("build", "run"))
