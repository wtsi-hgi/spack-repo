# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnnmap(RPackage):
	"""Genome annotation and visualisation package pertaining to Affymetrix arrays and NGS analysis.

	annmap provides annotation mappings for Affymetrix exon arrays and coordinate based queries to support deep sequencing data analysis. Database access is hidden behind the API which provides a set of functions such as genesInRange(), geneToExon(), exonDetails(), etc. Functions to plot gene architecture and BAM file data are also provided. Underlying data are from Ensembl. The annmap database can be downloaded from: https://figshare.manchester.ac.uk/account/articles/16685071
	"""
	
	homepage = "https://github.com/cruk-mi/annmap"
	bioc = "annmap" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/annmap_1.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/annmap/annmap_1.44.0.tar.gz"]

	version("1.44.0", md5="4e793a7c30de8248f566e7c14bf3fa90")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rmysql@0.6.0:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
