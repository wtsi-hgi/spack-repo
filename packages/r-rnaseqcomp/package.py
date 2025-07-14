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

	version("1.38.0", commit="b51afcd3b766aaa6ceee4cd389c18c9443a21e18")
	version("1.32.0", commit="05f2020b991c7cd2358f79b50d0271621d73a4c3")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
