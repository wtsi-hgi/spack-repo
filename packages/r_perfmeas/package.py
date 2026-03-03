# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPerfmeas(RPackage):
	"""Performance Measures for Ranking and Classification Tasks

	Implementation of different performance measures for classification and ranking tasks  including  Area Under the Receiving Characteristic Curve (AUROC) and Area Under the Precision Recall Curve (AUPRC), precision at a given recall, F-score for single and multiple classes.
	"""
	
	cran = "PerfMeas" 

	version("1.2.5", md5="51bf01d4cce4aac88147ee87e71d2a9b")

	depends_on("r-limma", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
