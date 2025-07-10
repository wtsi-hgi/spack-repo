# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHeron(RPackage):
	"""Hierarchical Epitope pROtein biNding

	HERON is a software package for analyzing peptide binding array data. In addition to identifying significant binding probes, HERON also provides functions for finding epitopes (string of consecutive peptides within a protein). HERON also calculates significance on the probe, epitope, and protein level by employing meta p-value methods.  HERON is designed for obtaining calls on the sample level and calculates fractions of hits for different conditions.
	"""
	
	homepage = "https://github.com/Ong-Research/HERON"
	bioc = "HERON" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/HERON_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/HERON/HERON_1.0.0.tar.gz"]

	version("1.0.0", sha256="b1a365540c32dac743dc87e5428e26692fd7174ec8a76f014d19e727ab60e34b")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-summarizedexperiment@1.1.6:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-harmonicmeanp", type=("build", "run"))
	depends_on("r-metap", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
