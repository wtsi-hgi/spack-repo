# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnvgsa(RPackage):
	"""Gene Set Analysis of (Rare) Copy Number Variants

	This package is intended to facilitate gene-set association with rare CNVs in case-control studies.
	"""
	
	bioc = "cnvGSA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/cnvGSA_1.46.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/cnvGSA/cnvGSA_1.46.0.tar.gz"]

	version("1.46.0", sha256="7aecf6d5c195b51aefac506a1be5ef5a8bf2a0394e12f67b3c32e4c11e2addce")

	depends_on("r-brglm", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-splitstackshape", type=("build", "run"))
