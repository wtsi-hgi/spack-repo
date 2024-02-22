# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWordpiece(RPackage):
	"""R Implementation of Wordpiece Tokenization

	Apply 'Wordpiece' (<arXiv:1609.08144>) tokenization to input text, 
 given an appropriate vocabulary. The 'BERT' (<arXiv:1810.04805>) tokenization 
 conventions are used by default.
	"""
	
	homepage = "https://github.com/macmillancontentscience/wordpiece"
	cran = "wordpiece" 

	version("2.1.3", md5="1916c5a74106ce2f1e7063ac1b112a24")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dlr@1:", type=("build", "run"))
	depends_on("r-fastmatch@1.1:", type=("build", "run"))
	depends_on("r-memoise@2:", type=("build", "run"))
	depends_on("r-piecemaker@1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringi@1:", type=("build", "run"))
	depends_on("r-wordpiece-data@1.0.2:", type=("build", "run"))
