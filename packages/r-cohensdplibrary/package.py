# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCohensdplibrary(RPackage):
	"""Cohen's D_p Computation with Confidence Intervals

	Computing Cohen's d_p in any experimental designs (between-subject, within-subject, and single-group design). Cousineau (2022) <https://github.com/dcousin3/CohensdpLibrary>; Cohen (1969, ISBN: 0-8058-0283-5).
	"""
	
	cran = "CohensdpLibrary" 

	version("0.5.10", md5="75b9642cb616bfc2f6bd3fa70c44862f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
