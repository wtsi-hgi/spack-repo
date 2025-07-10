# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAspli(RPackage):
	"""Analysis of Alternative Splicing Using RNA-Seq

	Integrative pipeline for the analysis of alternative splicing using RNAseq.
	"""
	
	bioc = "ASpli" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ASpli_2.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ASpli/ASpli_2.12.0.tar.gz"]

	version("2.12.0", sha256="5e9ec698127d453cde27310b815b047da4114e0c89a00032104c38b7f7004166")

	depends_on("r-edger", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-gviz", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-upsetr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pbmcapply", type=("build", "run"))
