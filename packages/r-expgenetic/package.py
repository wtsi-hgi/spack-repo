# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExpgenetic(RPackage):
	"""Non-Additive Expression Analysis of Hybrid Offspring

	Three functional modules, including genetic features, differential expression analysis and non-additive expression analysis were integrated into the package. And the package is suitable for RNA-seq and small RNA sequencing data. Besides, two methods of non-additive expression analysis were provided. One is the calculation of the additive (a) and dominant (d), the other is the evaluation of expression level dominance by comparing the total expression of the gene in hybrid offspring with the expression level in parents. For non-additive expression analysis of RNA-seq data, it is only applicable to hybrid offspring (including two sub-genomes) species for the time being.
	"""
	
	cran = "ExpGenetic" 

	version("0.1.0", md5="c2b9fd3c57a01e94f7a0860cde5e5be5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-deseq2@1.34:", type=("build", "run"))
	depends_on("r-futile-logger@1.4.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.6:", type=("build", "run"))
	depends_on("r-ggsci@2.9:", type=("build", "run"))
	depends_on("r-plyr@1.8.7:", type=("build", "run"))
	depends_on("r-venndiagram@1.7.3:", type=("build", "run"))
