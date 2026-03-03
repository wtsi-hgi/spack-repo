# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiolink(RPackage):
	"""Create Hyperlinks to Biological Databases and Resources

	Generate urls and hyperlinks to commonly used biological databases
    and resources based on standard identifiers. This is primarily useful when
    writing dynamic reports that reference things like gene symbols in text or
    tables, allowing you to, for example, convert gene identifiers to hyperlinks
    pointing to their entry in the 'NCBI' Gene database. Currently supports
    'NCBI' Gene, 'PubMed', Gene Ontology, 'KEGG', CRAN and Bioconductor.
	"""
	
	cran = "biolink" 

	version("0.1.8", md5="46ce81f7e89ac604735b5e400a67d2da")

	depends_on("r-rentrez", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rmysql", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
