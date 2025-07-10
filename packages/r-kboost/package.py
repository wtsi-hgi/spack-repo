# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKboost(RPackage):
	"""Inference of gene regulatory networks from gene expression data

	Reconstructing gene regulatory networks and transcription factor activity is crucial to understand biological processes and holds potential for developing personalized treatment. Yet, it is still an open problem as state-of-art algorithm are often not able to handle large amounts of data. Furthermore, many of the present methods predict numerous false positives and are unable to integrate other sources of information such as previously known interactions. Here we introduce KBoost, an algorithm that uses kernel PCA regression, boosting and Bayesian model averaging for fast and accurate reconstruction of gene regulatory networks. KBoost can also use a prior network built on previously known transcription factor targets. We have benchmarked KBoost using three different datasets against other high performing algorithms. The results show that our method compares favourably to other methods across datasets.
	"""
	
	homepage = "https://github.com/Luisiglm/KBoost"
	bioc = "KBoost" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/KBoost_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/KBoost/KBoost_1.10.0.tar.gz"]

	version("1.10.0", sha256="1132da444f04934200dd92483b478116c51d9a995b698648e88b97b109086de9")

	depends_on("r@4.1:", type=("build", "run"))
