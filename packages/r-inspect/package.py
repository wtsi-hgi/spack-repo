# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInspect(RPackage):
	"""Modeling RNA synthesis, processing and degradation with RNA-seq data

	INSPEcT (INference of Synthesis, Processing and dEgradation rates from Transcriptomic data) RNA-seq data in time-course experiments or steady-state conditions, with or without the support of nascent RNA data.
	"""
	
	bioc = "INSPEcT" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/INSPEcT_1.32.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/INSPEcT/INSPEcT_1.32.1.tar.gz"]

	version("1.32.1", sha256="90019156251074200fd27dc0b317b8e06c530b71904c8f05ab0c946b2653f613")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-plgem", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-txdb-mmusculus-ucsc-mm9-knowngene", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
