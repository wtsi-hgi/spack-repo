# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBgeecall(RPackage):
	"""Automatic RNA-Seq present/absent gene expression calls generation

	BgeeCall allows to generate present/absent gene expression calls without using an arbitrary cutoff like TPM<1. Calls are generated based on reference intergenic sequences. These sequences are generated based on expression of all RNA-Seq libraries of each species integrated in Bgee (https://bgee.org).
	"""
	
	homepage = "https://github.com/BgeeDB/BgeeCall"
	bioc = "BgeeCall" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/BgeeCall_1.18.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/BgeeCall/BgeeCall_1.18.1.tar.gz"]

	version("1.18.1", md5="d6ffd11b71faf135832b99515c7ba4cd")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-tximport", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-sjmisc", type=("build", "run"))
	depends_on("r-rslurm", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("kallisto", type=("build", "link", "run"))
