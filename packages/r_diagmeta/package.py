# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiagmeta(RPackage):
	"""Meta-Analysis of Diagnostic Accuracy Studies with Several
Cutpoints

	Provides methods by Steinhauser et al. (2016) <DOI:10.1186/s12874-016-0196-1> for meta-analysis of diagnostic accuracy studies with several cutpoints.
	"""
	
	homepage = "https://github.com/guido-s/diagmeta"
	cran = "diagmeta" 

	version("0.5-1", md5="66abc479c1e7a19d7b3322983ee75e06")

	depends_on("r-meta@5.0.0:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
