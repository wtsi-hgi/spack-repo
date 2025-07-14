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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RSeqAn_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RSeqAn/RSeqAn_1.22.0.tar.gz"]

	version("1.28.0", tag="RELEASE_3_21")
	version("1.22.0", sha256="24ff6104f19069b26e2c34f9ba0455610ba36a961ead1e9db3a89d01ba918873")

	depends_on("r-rcpp", type=("build", "run"))
