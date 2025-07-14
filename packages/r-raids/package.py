# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRaids(RPackage):
	"""Accurate Inference of Genetic Ancestry from Cancer Sequences

	This package implements specialized algorithms that enable genetic ancestry inference from various cancer sequences sources (RNA, Exome and Whole-Genome sequences). This package also implements a simulation algorithm that generates synthetic cancer-derived data. This code and analysis pipeline was designed and developed for the following publication: Belleau, P et al. Genetic Ancestry Inference from Cancer-Derived Molecular Data across Genomic and Transcriptomic Platforms. Cancer Res 1 January 2023; 83 (1): 49–58.
	"""
	
	homepage = "https://krasnitzlab.github.io/RAIDS/"
	bioc = "RAIDS" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RAIDS_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RAIDS/RAIDS_1.0.0.tar.gz"]

    version("1.6.1", tag="RELEASE_3_21")
	version("1.0.0", sha256="0208eb91f74930bbcebbec4844b708878391831b9097c0080d36cce9c78c5799")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-gdsfmt", type=("build", "run"))
	depends_on("r-snprelate", type=("build", "run"))
	depends_on("r-genesis", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ensembldb", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-annotationfilter", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-matrixgenerics", type=("build", "run"))
