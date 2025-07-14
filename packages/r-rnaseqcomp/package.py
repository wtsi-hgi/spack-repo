# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnaseqcomp(RPackage):
	"""Benchmarks for RNA-seq Quantification Pipelines

	Several quantitative and visualized benchmarks for RNA-seq quantification pipelines. Two-condition quantifications for genes, transcripts, junctions or exons by each pipeline with necessary meta information should be organized into numeric matrices in order to proceed the evaluation.
	"""
	
	homepage = "https://github.com/tengmx/rnaseqcomp"
	bioc = "rnaseqcomp" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/rnaseqcomp_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/rnaseqcomp/rnaseqcomp_1.32.0.tar.gz"]

    version("1.38.0", tag="RELEASE_3_21")
	version("1.32.0", sha256="be01564bef64eda55c7334a3c37adbea403b4e686f1f2db3576185d207bdd47a")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
