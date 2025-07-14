# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClomial(RPackage):
	"""Infers clonal composition of a tumor

	Clomial fits binomial distributions to counts obtained from Next Gen Sequencing data of multiple samples of the same tumor. The trained parameters can be interpreted to infer the clonal structure of the tumor.
	"""
	
	bioc = "Clomial"

	version("1.44.0", commit="d9dd6264663dcaa2fcaedda798f36dc840661613")
	version("1.38.0", commit="8f3c0843ade320a536864a0adeec5b8695480b4b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-permute", type=("build", "run"))
