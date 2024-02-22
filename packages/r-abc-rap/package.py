# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbcRap(RPackage):
	"""Array Based CpG Region Analysis Pipeline

	It aims to identify candidate genes that are “differentially
    methylated” between cases and controls. It applies Student’s t-test and delta beta analysis to
    identify candidate genes containing multiple “CpG sites”.
	"""
	
	cran = "ABC.RAP" 

	version("0.9.0", md5="38c65a7251d28ef2462ee430ded95700")

	depends_on("r@3.1:", type=("build", "run"))
