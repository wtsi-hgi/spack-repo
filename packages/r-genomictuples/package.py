# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomictuples(RPackage):
	"""Representation and Manipulation of Genomic Tuples

	GenomicTuples defines general purpose containers for storing genomic tuples. It aims to provide functionality for tuples of genomic co-ordinates that are analogous to those available for genomic ranges in the GenomicRanges Bioconductor package.
	"""
	
	homepage = "www.github.com/PeteHaitch/GenomicTuples"
	bioc = "GenomicTuples"

	version("1.42.0", commit="1c0aea79be7ad1fc79708ce48344f63ce05c881e")
	version("1.36.0", commit="736a13aa2765ae2c4dc970a170d080e4cb587168")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-genomicranges@1.37.4:", type=("build", "run"))
	depends_on("r-genomeinfodb@1.15.2:", type=("build", "run"))
	depends_on("r-s4vectors@0.17.25:", type=("build", "run"))
	depends_on("r-biocgenerics@0.21.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-iranges@2.19.13:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
