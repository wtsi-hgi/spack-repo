# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQdnaseqMm10(RPackage):
	"""Bin annotation mm10

	This package provides QDNAseq bin annotations for the mouse genome build mm10.
	"""
	
	homepage = "https://github.com/tgac-vumc/QDNAseq.mm10"
	bioc = "QDNAseq.mm10" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/QDNAseq.mm10_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/QDNAseq.mm10/QDNAseq.mm10_1.32.0.tar.gz"]

	version("1.32.0", sha256="e6dda2030d080e0168dc7c3475590ef79f3ef54bf8781c4864382cdc2bb3a474", url="https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/QDNAseq.mm10_1.32.0.tar.gz")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-qdnaseq", type=("build", "run"))

