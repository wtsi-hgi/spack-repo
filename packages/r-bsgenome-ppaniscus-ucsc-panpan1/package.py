# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomePpaniscusUcscPanpan1(RPackage):
	"""Full genome sequences for Pan paniscus (UCSC version panPan1)

	Full genome sequences for Pan paniscus (Bonobo) as provided by UCSC (panPan1, May 2012) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Ppaniscus.UCSC.panPan1" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Ppaniscus.UCSC.panPan1_1.4.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Ppaniscus.UCSC.panPan1/BSgenome.Ppaniscus.UCSC.panPan1_1.4.3.tar.gz"]

	version("1.4.3", sha256="ac4215a4c0fc8a7cb942615e887be462afca729567f707d131bbca32e2a49069", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Ppaniscus.UCSC.panPan1_1.4.3.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

