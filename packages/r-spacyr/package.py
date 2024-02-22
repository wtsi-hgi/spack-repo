# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpacyr(RPackage):
	"""Wrapper to the 'spaCy' 'NLP' Library

	An R wrapper to the 'Python' 'spaCy' 'NLP' library,
    from <https://spacy.io>.
	"""
	
	homepage = "https://spacyr.quanteda.io"
	cran = "spacyr" 

	version("1.3.0", md5="1a791b08b3e402ca258ee45d148f4be5")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-reticulate@1.6:", type=("build", "run"))
