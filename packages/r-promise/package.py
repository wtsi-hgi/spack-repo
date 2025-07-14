# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPromise(RPackage):
	"""PRojection Onto the Most Interesting Statistical Evidence

	A general tool to identify genomic features with a specific biologically interesting pattern of associations with multiple endpoint variables as described in Pounds et. al. (2009) Bioinformatics 25: 2013-2019
	"""
	
	bioc = "PROMISE"

	version("1.60.0", commit="1bf44aa3418ed14ff8b3b51619834eb1a27e3e79")
	version("1.54.0", commit="1fbb7d79fd07e960139aaaeadd59d99d69ebb18a")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
