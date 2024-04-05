# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAhpubmeddbs(RPackage):
	"""SQLites, tibbles, and data.tables for AnnotationHub

	Supplies AnnotationHub with some preprocessed sqlite, tibble, and data.table datasets of PubMed. All the datasets are generated by our Snakemake workflow [pubmed-workflow](https://github.com/rikenbit/pubmed-workflow). For the details, see the README.md of pubmed-workflow.
	"""
	
	bioc = "AHPubMedDbs" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/AHPubMedDbs_1.7.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/AHPubMedDbs/AHPubMedDbs_1.7.0.tar.gz"]

	version("1.7.0", md5="b2db2eda6009bc9cdec579c4ab579f25")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-annotationhub@2.22:", type=("build", "run"))

