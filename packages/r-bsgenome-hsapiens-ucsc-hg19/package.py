# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeHsapiensUcscHg19(RPackage):
	"""Full genome sequences for Homo sapiens (UCSC version hg19, based on
	GRCh37.p13).

	Full genome sequences for Homo sapiens (Human) as provided by UCSC
	(hg19, Feb. 2009) and stored in Biostrings objects."""

	# This is a bioconductor package but there is no available git repo.
	bioc = "BSgenome.Hsapiens.UCSC.hg19"
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Hsapiens.UCSC.hg19_1.4.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Hsapiens.UCSC.hg19/BSgenome.Hsapiens.UCSC.hg19_1.4.3.tar.gz"]

	version("1.4.3", md5="bb3f864ab32450d895816b45f6105f4f", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Hsapiens.UCSC.hg19_1.4.3.tar.gz")
	version("1.4.3", md5="bb3f864ab32450d895816b45f6105f4f", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Hsapiens.UCSC.hg19_1.4.3.tar.gz")
	version(
		"1.4.3",
		url="https://bioconductor.org/packages/3.12/data/annotation/src/contrib/BSgenome.Hsapiens.UCSC.hg19_1.4.3.tar.gz",
		sha256="5bfa65d7836449d9b30c356968497cdfaa98be48c4e329e71e8f8a120f3e9d1a",
	)
		"1.4.0",
		url="https://bioconductor.org/packages/3.10/data/annotation/src/contrib/BSgenome.Hsapiens.UCSC.hg19_1.4.0.tar.gz",
		sha256="88f515e5c27dd11d10654250e3a0a9389e4dfeb0b1c2d43419aa7086e6c516f8",
	)

	depends_on("r-bsgenome", type=("build", "run"))

