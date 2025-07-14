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

	version("1.36.0", commit="a323878dfed4a7e981d8dece78cb3864ba4e434e")
	version("1.30.0", commit="85a36387f7e1dbeed3f8f9e958faffa12d393e50")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-epivizr@2.3.6:", type=("build", "run"))
	depends_on("r-git2r", type=("build", "run"))
	depends_on("r-epivizrserver", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
