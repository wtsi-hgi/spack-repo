# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsaface(RPackage):
	"""Moving Subset Analysis FACE

	The new methodology "moving subset analysis" provides functions to investigate the effect of environmental conditions on the CO2 fertilization effect within longterm free air carbon enrichment (FACE)  experiments. In general, the functionality is applicable to derive the influence of a third variable (forcing experiment-support variable) on the relation between a dependent and an independent variable.
	"""
	
	cran = "msaFACE" 

	version("0.1.0", md5="75501177f68186c5814350e564511e17")

	depends_on("r@2.10:", type=("build", "run"))
