# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAhlrbasedbs(RPackage):
	"""LRBaseDbs for AnnotationHub

	Supplies AnnotationHub with `LRbaseDb` Ligand-Receptor annotation databases for many species. All the SQLite files are generated by our Snakemake workflow [lrbase-workflow](https://github.com/rikenbit/lrbase-workflow). For the details, see the README.md of lrbase-workflow.
	"""
	
	bioc = "AHLRBaseDbs" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/AHLRBaseDbs_1.7.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/AHLRBaseDbs/AHLRBaseDbs_1.7.0.tar.gz"]

	version("1.7.0", md5="5df6ef84988477d6262e54abd07c82da")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-annotationhub@2.22:", type=("build", "run"))

	# annotation