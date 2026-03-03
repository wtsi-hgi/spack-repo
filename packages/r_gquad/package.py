# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGquad(RPackage):
	"""Prediction of G Quadruplexes and Other Non-B DNA Motifs

	Genomic biology is not limited to the confines of the canonical B-forming DNA duplex, but includes over ten different types of other secondary structures that are collectively termed non-B DNA structures. Of these non-B DNA structures, the G-quadruplexes are highly stable four-stranded structures that are recognized by distinct subsets of nuclear factors. This package provide functions for predicting intramolecular G quadruplexes. In addition, functions for predicting other intramolecular nonB DNA structures are included.
	"""
	
	cran = "gquad" 

	version("2.1-2", md5="60bdaa6107f49450812fdcbdd961015c")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-ape@5.6.2:", type=("build", "run"))
	depends_on("r-seqinr@4.2.23:", type=("build", "run"))
