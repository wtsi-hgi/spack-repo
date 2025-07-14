# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCustomprodb(RPackage):
	"""Generate customized protein database from NGS data, with a focus on RNA-Seq data, for proteomics search

	Database search is the most widely used approach for peptide and protein identification in mass spectrometry-based proteomics studies. Our previous study showed that sample-specific protein databases derived from RNA-Seq data can better approximate the real protein pools in the samples and thus improve protein identification. More importantly, single nucleotide variations, short insertion and deletions and novel junctions identified from RNA-Seq data make protein database more complete and sample-specific. Here, we report an R package customProDB that enables the easy generation of customized databases from RNA-Seq data for proteomics search. This work bridges genomics and proteomics studies and facilitates cross-omics data integration.
	"""
	
	bioc = "customProDB" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/customProDB_1.42.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/customProDB/customProDB_1.42.1.tar.gz"]

    version("1.48.0", tag="RELEASE_3_21")
	version("1.42.1", sha256="28be9c341aa2bc3e2c89560f041c5c3c23e6018de4591949f91a22043b3b51fc")
	version("1.41.0", md5="08f0eb20ac48a7b8f1e27b45522dd029")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biomart@2.17.1:", type=("build", "run"))
	depends_on("r-s4vectors@0.9.25:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rsamtools@1.10.2:", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-biostrings@2.26.3:", type=("build", "run"))
	depends_on("r-genomicfeatures@1.32:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-variantannotation@1.13.44:", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-ahocorasicktrie", type=("build", "run"))
