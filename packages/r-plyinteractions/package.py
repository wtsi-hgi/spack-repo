# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlyinteractions(RPackage):
	"""Extending tidy verbs to genomic interactions

	Operate on `GInteractions` objects as tabular data using `dplyr`-like verbs. The functions and methods in `plyinteractions` provide a grammatical approach to manipulate `GInteractions`, to facilitate their integration in genomic analysis workflows.
	"""
	
	homepage = "https://github.com/js2264/plyinteractions"
	bioc = "plyinteractions" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/plyinteractions_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/plyinteractions/plyinteractions_1.0.0.tar.gz"]

	version("1.0.0", sha256="26c741611517bc92e1a09cacf650b64b5beef28ee3e4eabf9d21efe995ad21b8")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-interactionset", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-plyranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
