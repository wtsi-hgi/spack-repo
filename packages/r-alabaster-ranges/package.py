# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlabasterRanges(RPackage):
	"""Load and Save Ranges-related Artifacts from File

	Save GenomicRanges, IRanges and related data structures into file artifacts, and load them back into memory. This is a more portable alternative to serialization of such objects into RDS files. Each artifact is associated with metadata for further interpretation; downstream applications can enrich this metadata with context-specific properties.
	"""
	
	bioc = "alabaster.ranges" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/alabaster.ranges_1.2.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/alabaster.ranges/alabaster.ranges_1.2.0.tar.gz"]

	version("1.2.0", md5="af5d849080999b0167cc39fc182721e9")

	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-alabaster-base", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
