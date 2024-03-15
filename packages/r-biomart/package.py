# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiomart(RPackage):
	"""Interface to BioMart databases (i.e. Ensembl).

	In recent years a wealth of biological data has become available in
	public data repositories. Easy access to these valuable data resources
	and firm integration with data analysis is needed for comprehensive
	bioinformatics data analysis. biomaRt provides an interface to a growing
	collection of databases implementing the BioMart software suite
	(<http://www.biomart.org>). The package enables retrieval of large
	amounts of data in a uniform way without the need to know the underlying
	database schemas or write complex SQL queries. The most prominent
	examples of BioMart databases are maintain by Ensembl, which provides
	biomaRt users direct access to a diverse set of data and enables a wide
	range of powerful online queries from gene annotation to database
	mining."""

	bioc = "biomaRt"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/biomaRt_2.58.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/biomaRt/biomaRt_2.58.2.tar.gz"]

	version("2.58.2", md5="9cd8b1d118761e837a3c037dcfafbfc2")

	depends_on("r-xml@3.99.0.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
