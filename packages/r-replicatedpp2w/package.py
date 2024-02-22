# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReplicatedpp2w(RPackage):
	"""Two-Way ANOVA-Like Method to Analyze Replicated Point Patterns

	Test for effects of  both individual factors and their interaction on  replicated spatial patterns in a two factorial design, as explained in Ramon et al. (2016) <doi:10.1111/ecog.01848>.
	"""
	
	cran = "replicatedpp2w" 

	version("0.1-5", md5="7629a8bf6ccd271b67d5574e87c5b0ac")

	depends_on("r-spatstat@2.0.0:", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-spatstat-utils", type=("build", "run"))
