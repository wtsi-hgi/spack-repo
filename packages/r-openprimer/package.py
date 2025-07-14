# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpenprimer(RPackage):
	"""Multiplex PCR Primer Design and Analysis

	An implementation of methods for designing, evaluating, and comparing primer sets for multiplex PCR. Primers are designed by solving a set cover problem such that the number of covered template sequences is maximized with the smallest possible set of primers. To guarantee that high-quality primers are generated, only primers fulfilling constraints on their physicochemical properties are selected. A Shiny app providing a user interface for the functionalities of this package is provided by the 'openPrimeRui' package.
	"""
	
	bioc = "openPrimeR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/openPrimeR_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/openPrimeR/openPrimeR_1.24.0.tar.gz"]

    version("1.30.0", tag="RELEASE_3_21")
	version("1.24.0", sha256="8d5069817ea94f2293d7e54bf01a97e5e0896c111f2229c954c7cf932f32f84a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biostrings@2.38.4:", type=("build", "run"))
	depends_on("r-xml@3.98.1.4:", type=("build", "run"))
	depends_on("r-scales@0.4:", type=("build", "run"))
	depends_on("r-reshape2@1.4.1:", type=("build", "run"))
	depends_on("r-seqinr@3.3.3:", type=("build", "run"))
	depends_on("r-iranges@2.4.8:", type=("build", "run"))
	depends_on("r-genomicranges@1.22.4:", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-dplyr@0.5:", type=("build", "run"))
	depends_on("r-stringdist@0.9.4.1:", type=("build", "run"))
	depends_on("r-stringr@1:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-decipher@1.16.1:", type=("build", "run"))
	depends_on("r-lpsolveapi@5.5.2.0.17:", type=("build", "run"))
	depends_on("r-digest@0.6.9:", type=("build", "run"))
	depends_on("r-hmisc@3.17.4:", type=("build", "run"))
	depends_on("r-ape@3.5:", type=("build", "run"))
	depends_on("r-biocgenerics@0.16.1:", type=("build", "run"))
	depends_on("r-s4vectors@0.8.11:", type=("build", "run"))
	depends_on("r-foreach@1.4.3:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-distr@2.6:", type=("build", "run"))
	depends_on("r-distrex@2.6:", type=("build", "run"))
	depends_on("r-fitdistrplus@1.0.7:", type=("build", "run"))
	depends_on("r-uniqtag@1:", type=("build", "run"))
	depends_on("r-openxlsx@4.0.17:", type=("build", "run"))
	depends_on("mafft@7.305:", type=("build", "link", "run"))
	depends_on("viennarna@2.4.1:", type=("build", "link", "run"))
	depends_on("pandoc@1.12.3:", type=("build", "link", "run"))
