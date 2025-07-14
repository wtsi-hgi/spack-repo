# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiffcoexp(RPackage):
	"""Differential Co-expression Analysis

	A tool for the identification of differentially coexpressed links (DCLs) and differentially coexpressed genes (DCGs). DCLs are gene pairs with significantly different correlation coefficients under two conditions. DCGs are genes with significantly more DCLs than by chance.
	"""
	
	homepage = "https://github.com/hidelab/diffcoexp"
	bioc = "diffcoexp" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/diffcoexp_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/diffcoexp/diffcoexp_1.22.0.tar.gz"]

    version("1.28.0", tag="RELEASE_3_21")
	version("1.22.0", sha256="83bc24bc3489d7bd542806fdb8ab331734db9603335a235809032c505037ee41")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-wgcna", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-diffcorr", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
