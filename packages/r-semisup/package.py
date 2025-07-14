# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemisup(RPackage):
	"""Semi-Supervised Mixture Model

	Implements a parametric semi-supervised mixture model. The permutation test detects markers with main or interactive effects, without distinguishing them. Possible applications include genome-wide association analysis and differential expression analysis.
	"""
	
	homepage = "https://github.com/rauschenberger/semisup"
	bioc = "semisup" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/semisup_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/semisup/semisup_1.26.0.tar.gz"]

	version("1.32.0", tag="RELEASE_3_21")
	version("1.26.0", sha256="a9b0a2eb85fe87ff5f7397d5a966637f07cbbe66b88a1ebb72391cfef8676376")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
