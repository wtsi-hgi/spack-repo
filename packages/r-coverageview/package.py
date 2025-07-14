# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoverageview(RPackage):
	"""Coverage visualization package for R

	This package provides a framework for the visualization of genome coverage profiles. It can be used for ChIP-seq experiments, but it can be also used for genome-wide nucleosome positioning experiments or other experiment types where it is important to have a framework in order to inspect how the coverage distributed across the genome
	"""
	
	bioc = "CoverageView" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CoverageView_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CoverageView/CoverageView_1.40.0.tar.gz"]

	version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="eed2354ad19f145fbf629bf13538fb64fe1f44fde7d65ae07c7e694b50de41ea")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rsamtools@1.19.17:", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-s4vectors@0.7.21:", type=("build", "run"))
	depends_on("r-iranges@2.3.23:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
