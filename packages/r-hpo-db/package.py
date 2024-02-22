# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHpoDb(RPackage):
	"""A set of annotation maps describing the entire Human Phenotype Ontology

	Human Phenotype Ontology (HPO) was developed to create a consistent description of gene products with disease perspectives, and is essential for supporting functional genomics in disease context. Accurate disease descriptions can discover new relationships between genes and disease, and new functions for previous uncharacteried genes and alleles.We have developed the [DOSE](https://bioconductor.org/packages/DOSE/) package for semantic similarity analysis and disease enrichment analysis, and `DOSE` import an Bioconductor package 'DO.db' to get the relationship(such as parent and child) between MPO terms. But `DO.db` hasn't been updated for years, and a lot of semantic information is [missing](https://github.com/YuLab-SMU/DOSE/issues/57). So we developed the new package `HPO.db` for Human Human Phenotype Ontology annotation.
	"""
	
	bioc = "HPO.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/HPO.db_0.99.2.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/HPO.db/HPO.db_0.99.2.tar.gz"]

	version("0.99.2", md5="977cfb31ff344c58fd2dd0a2c6b765ab")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))

	# annotation