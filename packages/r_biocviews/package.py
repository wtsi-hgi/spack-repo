# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiocviews(RPackage):
	"""Categorized views of R package repositories

	Infrastructure to support 'views' used to classify Bioconductor packages. 'biocViews' are directed acyclic graphs of terms from a controlled vocabulary. There are three major classifications, corresponding to 'software', 'annotation', and 'experiment data' packages.
	"""
	
	homepage = "http://bioconductor.org/packages/biocViews"
	bioc = "biocViews" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/biocViews_1.70.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/biocViews/biocViews_1.70.0.tar.gz"]

	version("1.70.0", md5="e258342a57f06fa23f3732c75539c58d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-graph@1.9.26:", type=("build", "run"))
	depends_on("r-rbgl@1.13.5:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-runit", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
