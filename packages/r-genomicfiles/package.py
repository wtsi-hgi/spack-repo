# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomicfiles(RPackage):
	"""Distributed computing by file or by range

	This package provides infrastructure for parallel computations distributed 'by file' or 'by range'. User defined MAPPER and REDUCER functions provide added flexibility for data combination and manipulation.
	"""
	
	bioc = "GenomicFiles" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GenomicFiles_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GenomicFiles/GenomicFiles_1.38.0.tar.gz"]

	version("1.44.1", tag="RELEASE_3_21")
	version("1.38.0", sha256="959bdb955c859bfd520a0a64f4541484c981237bceaa26b76c162c0881d17ecf")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-biocgenerics@0.11.2:", type=("build", "run"))
	depends_on("r-matrixgenerics", type=("build", "run"))
	depends_on("r-genomicranges@1.31.16:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocparallel@1.1:", type=("build", "run"))
	depends_on("r-rsamtools@1.17.29:", type=("build", "run"))
	depends_on("r-rtracklayer@1.25.3:", type=("build", "run"))
	depends_on("r-genomicalignments@1.7.7:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors@0.9.25:", type=("build", "run"))
	depends_on("r-variantannotation@1.27.9:", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
