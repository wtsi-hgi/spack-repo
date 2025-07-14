# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaqcexpression4plex(RPackage):
	"""Sample Expression Data - MAQC / HG18 - NimbleGen

	Data from human (HG18) 4plex NimbleGen array. It has 24k genes with 3 60mer probes per gene.
	"""
	
	bioc = "maqcExpression4plex" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/maqcExpression4plex_1.46.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/maqcExpression4plex/maqcExpression4plex_1.46.0.tar.gz"]

    version("1.52.0", tag="RELEASE_3_21")
	version("1.46.0", sha256="ac918856ce0d7a2d6b30c5ff0b628508f8ddfc003cc1d1cbd1dd0fd9ecaf1c46")


