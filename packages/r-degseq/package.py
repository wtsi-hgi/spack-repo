# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDegseq(RPackage):
	"""Identify Differentially Expressed Genes from RNA-seq data

	DEGseq is an R package to identify differentially expressed genes from RNA-Seq data.
	"""
	
	bioc = "DEGseq" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DEGseq_1.56.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/DEGseq/DEGseq_1.56.1.tar.gz"]

    version("1.62.0", tag="RELEASE_3_21")
	version("1.56.1", sha256="92c49cb54946dedeb3f1309f812d4d12c276e1e008b40c4e0940a37339d4657a")

	depends_on("r@2.8:", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
