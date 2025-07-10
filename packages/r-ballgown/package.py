# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBallgown(RPackage):
	"""Flexible, isoform-level differential expression analysis

	Tools for statistical analysis of assembled transcriptomes, including flexible differential expression analysis, visualization of transcript structures, and matching of assembled transcripts to annotation.
	"""
	
	bioc = "ballgown" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ballgown_2.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ballgown/ballgown_2.34.0.tar.gz"]

	version("2.34.0", sha256="658426a92661774c79ea1c80ab8a378682cf0c0c9a8acdb83e17fe93bcf978e4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges@1.17.25:", type=("build", "run"))
	depends_on("r-iranges@1.99.22:", type=("build", "run"))
	depends_on("r-s4vectors@0.9.39:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-rtracklayer@1.29.25:", type=("build", "run"))
	depends_on("r-biobase@2.25:", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
