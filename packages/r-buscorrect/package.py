# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBuscorrect(RPackage):
	"""Batch Effects Correction with Unknown Subtypes

	High-throughput experimental data are accumulating exponentially in public databases. However, mining valid scientific discoveries from these abundant resources is hampered by technical artifacts and inherent biological heterogeneity. The former are usually termed "batch effects," and the latter is often modelled by "subtypes." The R package BUScorrect fits a Bayesian hierarchical model, the Batch-effects-correction-with-Unknown-Subtypes model (BUS), to correct batch effects in the presence of unknown subtypes. BUS is capable of (a) correcting batch effects explicitly, (b) grouping samples that share similar characteristics into subtypes, (c) identifying features that distinguish subtypes, and (d) enjoying a linear-order computation complexity.
	"""
	
	bioc = "BUScorrect" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BUScorrect_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BUScorrect/BUScorrect_1.20.0.tar.gz"]

    version("1.26.0", tag="RELEASE_3_21")
	version("1.20.0", sha256="ee61d25c6558b9886fe58ee38c2c898abc19bfbccb54e5b71ba7b224455f7050")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
