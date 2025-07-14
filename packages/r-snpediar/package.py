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

	version("1.34.0", commit="8ad7fa3931c9be799c9403efc53a3b903c2a8d1e")
	version("1.28.0", commit="94a76d11f2756691997b917d83d72eb778b61479")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
