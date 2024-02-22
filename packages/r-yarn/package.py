# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYarn(RPackage):
	"""Robust Multi-Condition RNA-Seq Preprocessing and Normalization.

	Expedite large RNA-Seq analyses using a combination of previously
	developed tools. YARN is meant to make it easier for the user in
	performing basic mis-annotation quality control, filtering, and
	condition-aware normalization. YARN leverages many Bioconductor tools
	and statistical techniques to account for the large heterogeneity and
	sparsity found in very large RNA-seq experiments."""

	bioc = "yarn"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/yarn_1.28.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/yarn/yarn_1.28.0.tar.gz"]

	version("1.28.0", md5="90baa3de55a308d7deef0f913c6fdef8")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-downloader", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-quantro", type=("build", "run"))
