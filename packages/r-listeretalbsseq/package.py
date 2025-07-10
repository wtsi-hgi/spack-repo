# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RListeretalbsseq(RPackage):
	"""BS-seq data of H1 and IMR90 cell line excerpted from Lister et al. 2009

	Base resolution bisulfite sequencing data of Human DNA methylomes
	"""
	
	bioc = "ListerEtAlBSseq" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/ListerEtAlBSseq_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/ListerEtAlBSseq/ListerEtAlBSseq_1.34.0.tar.gz"]

	version("1.34.0", sha256="220de24447fb48ed713f799d944c4e0b0db5f9b7c3c3465021515d524a036897")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-methylpipe", type=("build", "run"))

