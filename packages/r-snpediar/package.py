# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnpediar(RPackage):
	"""Query data from SNPedia

	SNPediaR provides some tools for downloading and parsing data from the SNPedia web site <http://www.snpedia.com>. The implemented functions allow users to import the wiki text available in SNPedia pages and to extract the most relevant information out of them. If some information in the downloaded pages is not automatically processed by the library functions, users can easily implement their own parsers to access it in an efficient way.
	"""
	
	homepage = "https://github.com/genometra/SNPediaR"
	bioc = "SNPediaR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SNPediaR_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SNPediaR/SNPediaR_1.28.0.tar.gz"]

    version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="e14d4a3d4062210d2413212256acd9cf5c37a5b29b81af730e98e0de51c82bde")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
