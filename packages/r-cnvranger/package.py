# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnvranger(RPackage):
	"""Summarization and expression/phenotype association of CNV ranges

	The CNVRanger package implements a comprehensive tool suite for CNV analysis. This includes functionality for summarizing individual CNV calls across a population, assessing overlap with functional genomic regions, and association analysis with gene expression and quantitative phenotypes.
	"""
	
	bioc = "CNVRanger" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CNVRanger_1.18.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CNVRanger/CNVRanger_1.18.1.tar.gz"]

    version("1.24.2", tag="RELEASE_3_21")
	version("1.18.1", sha256="62525db41e24dfad543649cd135c84a80f21068fa66f2ca1687533654d1838f3")
	version("1.18.0", md5="3e68952c47447dfad311d1adf7b971d1")

	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-raggedexperiment", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-gdsarray", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-snprelate", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-gdsfmt", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-qqman", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
