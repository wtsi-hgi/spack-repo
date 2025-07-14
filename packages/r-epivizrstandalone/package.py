# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpivizrstandalone(RPackage):
	"""Run Epiviz Interactive Genomic Data Visualization App within R

	This package imports the epiviz visualization JavaScript app for genomic data interactive visualization. The 'epivizrServer' package is used to provide a web server running completely within R. This standalone version allows to browse arbitrary genomes through genome annotations provided by Bioconductor packages.
	"""
	
	bioc = "epivizrStandalone" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/epivizrStandalone_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/epivizrStandalone/epivizrStandalone_1.30.0.tar.gz"]

	version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="e3bb330626d357158de693acb779b74a5067b927e531e926bf0939389f1afa4c")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-epivizr@2.3.6:", type=("build", "run"))
	depends_on("r-git2r", type=("build", "run"))
	depends_on("r-epivizrserver", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
