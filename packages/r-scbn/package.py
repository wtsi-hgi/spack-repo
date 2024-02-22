# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScbn(RPackage):
	"""A statistical normalization method and differential expression analysis for RNA-seq data between different species

	This package provides a scale based normalization (SCBN) method to identify genes with differential expression between different species. It takes into account the available knowledge of conserved orthologous genes and the hypothesis testing framework to detect differentially expressed orthologous genes. The method on this package are described in the article 'A statistical normalization method and differential expression analysis for RNA-seq data between different species' by Yan Zhou, Jiadi Zhu, Tiejun Tong, Junhui Wang, Bingqing Lin, Jun Zhang (2018, pending publication).
	"""
	
	bioc = "SCBN" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/SCBN_1.20.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/SCBN/SCBN_1.20.0.tar.gz"]

	version("1.20.0", md5="c58ee707d9418bd3374773e2675efad7")

	depends_on("r@3.5:", type=("build", "run"))
