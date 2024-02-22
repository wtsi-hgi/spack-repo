# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhuassess(RPackage):
	"""Proportional Habitat Use Assessment

	Assessment of habitat selection by means of the permutation-based combination of sign tests (Fattorini et al., 2014 <DOI:10.1007/s10651-013-0250-7>). To exemplify the application of this procedure, habitat selection is assessed for a population of European Brown Hares settled in central Italy.
	"""
	
	cran = "phuassess" 

	version("1.1", md5="6b833efdae56addee592de1d0379b8bd")

	depends_on("r@3.1:", type=("build", "run"))
