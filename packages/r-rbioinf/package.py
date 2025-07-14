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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RBioinf_1.62.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RBioinf/RBioinf_1.62.0.tar.gz"]

	version("1.68.0", tag="RELEASE_3_21")
	version("1.62.0", sha256="5e20bd398b6b0e470d75db76d60d2ef1fdf39f5e2b644175e891aac2f95f76c5")

	depends_on("r-graph", type=("build", "run"))
