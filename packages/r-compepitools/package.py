# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCompepitools(RPackage):
	"""Tools for computational epigenomics

	Tools for computational epigenomics developed for the analysis, integration and simultaneous visualization of various (epi)genomics data types across multiple genomic regions in multiple samples.
	"""
	
	bioc = "compEpiTools" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/compEpiTools_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/compEpiTools/compEpiTools_1.36.0.tar.gz"]

    version("1.42.0", tag="RELEASE_3_21")
	version("1.36.0", sha256="4e24c1334f10851a375f14c10be9ede2e8c0d747e1110803873c93c5f05dbba5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-topgo", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-xvector", type=("build", "run"))
	depends_on("r-methylpipe", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
