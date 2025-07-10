# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimd(RPackage):
	"""Statistical Inferences with MeDIP-seq Data (SIMD) to infer the methylation level for each CpG site

	This package provides a inferential analysis method for detecting differentially expressed CpG sites in MeDIP-seq data. It uses statistical framework and EM algorithm, to identify differentially expressed CpG sites. The methods on this package are described in the article 'Methylation-level Inferences and Detection of Differential Methylation with Medip-seq Data' by Yan Zhou, Jiadi Zhu, Mingtao Zhao, Baoxue Zhang, Chunfu Jiang and Xiyan Yang (2018, pending publication).
	"""
	
	bioc = "SIMD" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SIMD_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SIMD/SIMD_1.20.0.tar.gz"]

	version("1.20.0", sha256="924fbe6d2bb750f10bf5c75a9227866c215cb70b80469f0be3d6a82a6699a12a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-methylmnm", type=("build", "run"))
