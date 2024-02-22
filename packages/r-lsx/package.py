# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLsx(RPackage):
	"""Semi-Supervised Algorithm for Document Scaling

	A word embeddings-based semi-supervised model for document scaling Watanabe (2020) <doi:10.1080/19312458.2020.1832976>.
    LSS allows users to analyze large and complex corpora on arbitrary dimensions with seed words exploiting efficiency of word embeddings (SVD, Glove).
    It can generate word vectors on a users-provided corpus or incorporate a pre-trained word vectors.
	"""
	
	cran = "LSX" 

	version("1.3.2", md5="6a518e7bec7835ce4f54cd098db9af2f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-quanteda@2:", type=("build", "run"))
	depends_on("r-quanteda-textstats", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-rsvd", type=("build", "run"))
	depends_on("r-rsparse", type=("build", "run"))
	depends_on("r-proxyc", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
