# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAhensdbs(RPackage):
	"""EnsDbs for AnnotationHub

	Supplies AnnotationHub with EnsDb Ensembl-based annotation databases for all species. EnsDb SQLite databases are generated separately from Ensembl MySQL databases using functions from the ensembldb package employing the Ensembl Perl API.
	"""
	
	bioc = "AHEnsDbs" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/AHEnsDbs_1.1.11.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/AHEnsDbs/AHEnsDbs_1.1.11.tar.gz"]

	version("1.1.11", md5="b062155b0b493e9cc311656222c7c39a")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ensembldb@1.99.10:", type=("build", "run"))
	depends_on("r-annotationhubdata@1.5.24:", type=("build", "run"))

	# annotation