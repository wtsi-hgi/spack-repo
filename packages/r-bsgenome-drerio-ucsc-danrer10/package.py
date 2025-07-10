# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeDrerioUcscDanrer10(RPackage):
	"""Full genome sequences for Danio rerio (UCSC version danRer10)

	Full genome sequences for Danio rerio (Zebrafish) as provided by UCSC (danRer10, Sep. 2014) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Drerio.UCSC.danRer10" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Drerio.UCSC.danRer10_1.4.2.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Drerio.UCSC.danRer10/BSgenome.Drerio.UCSC.danRer10_1.4.2.tar.gz"]

	version("1.4.2", sha256="fa53048c8a1a8307b97e92f0634c51c92abc5694e1ae97d6e3ae98de60ec34bf", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Drerio.UCSC.danRer10_1.4.2.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

