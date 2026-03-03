# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSegmentier(RPackage):
	"""Similarity-Based Segmentation of Multidimensional Signals

	A dynamic programming solution to segmentation based on
        maximization of arbitrary similarity measures within segments.
	The general idea, theory and this implementation are described in
	Machne, Murray & Stadler (2017) <doi:10.1038/s41598-017-12401-8>.
	In addition to the core algorithm, the package provides time-series
	processing and clustering functions as described in the publication.
	These are generally applicable where a `k-means` clustering yields
	meaningful results, and have been specifically developed for
	clustering of the Discrete Fourier Transform of periodic gene
	expression data (`circadian' or `yeast metabolic oscillations').
	This clustering approach is outlined in the supplemental material of
	Machne & Murray (2012) <doi:10.1371/journal.pone.0037906>), and here
	is used as a basis of segment similarity measures. Notably, the
	time-series processing and clustering functions can also be used as
	stand-alone tools, independent of segmentation, e.g., for 
        transcriptome data already mapped to genes.
	"""
	
	homepage = "https://github.com/raim/segmenTier"
	cran = "segmenTier" 

	version("0.1.2", md5="b9bb4f51fdef90935759f4970541a4ea")

	depends_on("r-rcpp", type=("build", "run"))
