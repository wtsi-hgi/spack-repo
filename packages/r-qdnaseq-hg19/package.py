# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQdnaseqHg19(RPackage):
	"""QDNAseq bin annotation for hg19

	This package provides QDNAseq bin annotations for the human genome build hg19.
	"""
	
	homepage = "https://github.com/tgac-vumc/QDNAseq.hg19"
	bioc = "QDNAseq.hg19" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/QDNAseq.hg19_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/QDNAseq.hg19/QDNAseq.hg19_1.32.0.tar.gz"]

	version("1.38.0", tag="RELEASE_3_21")
	version("1.32.0", sha256="28b7634354f4900b746b8a586ed7b0e9e57a472975816d6007355ee7e75ad605", url="https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/QDNAseq.hg19_1.32.0.tar.gz")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-qdnaseq", type=("build", "run"))

