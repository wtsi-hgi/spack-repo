# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSegmentseq(RPackage):
	"""Methods for identifying small RNA loci from high-throughput sequencing data

	High-throughput sequencing technologies allow the production of large volumes of short sequences, which can be aligned to the genome to create a set of matches to the genome. By looking for regions of the genome which to which there are high densities of matches, we can infer a segmentation of the genome into regions of biological significance. The methods in this package allow the simultaneous segmentation of data from multiple samples, taking into account replicate data, in order to create a consensus segmentation. This has obvious applications in a number of classes of sequencing experiments, particularly in the discovery of small RNA loci and novel mRNA transcriptome discovery.
	"""
	
	bioc = "segmentSeq" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/segmentSeq_2.36.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/segmentSeq/segmentSeq_2.36.0.tar.gz"]

	version("2.36.0", md5="f86ecc00eba08e4f13412c624d98697c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bayseq@2.9:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-shortread", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
