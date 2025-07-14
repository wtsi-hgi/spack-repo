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

	version("1.7.0", tag="RELEASE_3_21")
	version("1.1.11", sha256="1afc474ca376b90a3fe0fd6ce2605987b7c12a1e6384b64c53ce2844a25408d6")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ensembldb@1.99.10:", type=("build", "run"))
	depends_on("r-annotationhubdata@1.5.24:", type=("build", "run"))

