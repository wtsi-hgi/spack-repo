# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTransview(RPackage):
	"""Read density map construction and accession. Visualization of ChIPSeq and RNASeq data sets

	This package provides efficient tools to generate, access and display read densities of sequencing based data sets such as from RNA-Seq and ChIP-Seq.
	"""
	
	homepage = "http://bioconductor.org/packages/release/bioc/html/TransView.html"
	bioc = "TransView"

	version("1.52.0", commit="6404ded573dd6aef3dc7b98d3db2a9ec14275c04")
	version("1.46.0", commit="2a55784aa940fc26b6ccb9a4ae47469af6593387")

	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors@0.9.25:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-rhtslib@1.99.1:", type=("build", "run"))
	depends_on("bzip2", type=("build", "link", "run"))
	depends_on("curl", type=("build", "link", "run"))
	depends_on("xz", type=("build", "link", "run"))
