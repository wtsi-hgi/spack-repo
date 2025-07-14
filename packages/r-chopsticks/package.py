# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChopsticks(RPackage):
	"""The 'snp.matrix' and 'X.snp.matrix' Classes

	Implements classes and methods for large-scale SNP association studies
	"""
	
	homepage = "http://outmodedbonsai.sourceforge.net/"
	bioc = "chopsticks"

	version("1.74.0", commit="df8f088dad25f8cdb75cd815dbc6badd490535d0")
	version("1.68.0", commit="dfe5d1274f7c70dfb79e5eb48e99aa74d009487c")

	depends_on("r-survival", type=("build", "run"))
