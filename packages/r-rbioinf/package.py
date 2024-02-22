# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbioinf(RPackage):
	"""RBioinf

	Functions and datasets and examples to accompany the monograph R For Bioinformatics.
	"""
	
	bioc = "RBioinf" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/RBioinf_1.62.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/RBioinf/RBioinf_1.62.0.tar.gz"]

	version("1.62.0", md5="ec036823fe8f50106f37436eec716add")

	depends_on("r-graph", type=("build", "run"))
