# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRseqan(RPackage):
	"""R SeqAn

	Headers and some wrapper functions from the SeqAn C++ library for ease of usage in R.
	"""
	
	bioc = "RSeqAn" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/RSeqAn_1.22.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/RSeqAn/RSeqAn_1.22.0.tar.gz"]

	version("1.22.0", md5="278ce2c8087516d02a4203bdcf9a6b9f")

	depends_on("r-rcpp", type=("build", "run"))
