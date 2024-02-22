# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPiecemaker(RPackage):
	"""Tools for Preparing Text for Tokenizers

	Tokenizers break text into pieces that are more usable by
    machine learning models. Many tokenizers share some preparation steps.
    This package provides those shared steps, along with a simple
    tokenizer.
	"""
	
	homepage = "https://github.com/macmillancontentscience/piecemaker"
	cran = "piecemaker" 

	version("1.0.2", md5="76338b05c3c123619a44def98173b73b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rlang@0.4.2:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
