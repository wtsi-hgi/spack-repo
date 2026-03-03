# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPromethee123(RPackage):
	"""PROMETHEE I, II, and III Methods

	The PROMETHEE method is a multi-criteria decision-making method addressing with outranking problems.
            The method establishes a preference structure between the alternatives, having a preference function for
            each criterion. IN this context, three variants of the method is carried out: PROMETHEE I (Partial Outranking),
            PROMETHEE II (Total Outranking), and PROMETHEE III (Outranking by Intervals). 
	"""
	
	cran = "promethee123" 

	version("0.1.0", md5="e717e0b697e9fb918f97b38bf98878e3", url="https://cran.r-project.org/src/contrib/promethee123_0.1.0.tar.gz")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
