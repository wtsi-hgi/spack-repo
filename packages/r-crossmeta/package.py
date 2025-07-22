# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrossmeta(RPackage):
	"""Cross Platform Meta-Analysis of Microarray Data

	Implements cross-platform and cross-species meta-analyses of Affymentrix, Illumina, and Agilent microarray data. This package automates common tasks such as downloading, normalizing, and annotating raw GEO data. The user then selects control and treatment samples in order to perform differential expression analyses for all comparisons. After analysing each contrast seperately, the user can select tissue sources for each contrast and specify any tissue sources that should be grouped for the subsequent meta-analyses.
	"""
	
	homepage = "https://github.com/alexvpickering/crossmeta"
	bioc = "crossmeta" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/crossmeta_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/crossmeta/crossmeta_1.28.0.tar.gz"]

    version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="bd7e53eb0e20b6b7b51b4959c07bf1d00851ee1b2f277e6001adc20e17d806a3")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-affy@1.52:", type=("build", "run"))
	depends_on("r-affxparser@1.46:", type=("build", "run"))
	depends_on("r-annotationdbi@1.36.2:", type=("build", "run"))
	depends_on("r-biobase@2.34:", type=("build", "run"))
	depends_on("r-biocgenerics@0.20:", type=("build", "run"))
	depends_on("r-biocmanager@1.30.4:", type=("build", "run"))
	depends_on("r-dt@0.2:", type=("build", "run"))
	depends_on("r-dbi@1:", type=("build", "run"))
	depends_on("r-data-table@1.10.4:", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-fdrtool@1.2.15:", type=("build", "run"))
	depends_on("r-geoquery@2.40:", type=("build", "run"))
	depends_on("r-limma@3.30.13:", type=("build", "run"))
	depends_on("r-matrixstats@0.51:", type=("build", "run"))
	depends_on("r-metama@3.1.2:", type=("build", "run"))
	depends_on("r-miniui@0.1.1:", type=("build", "run"))
	depends_on("r-oligo@1.38:", type=("build", "run"))
	depends_on("r-reader@1.0.6:", type=("build", "run"))
	depends_on("r-rcurl@1.95.4.11:", type=("build", "run"))
	depends_on("r-rsqlite@2.1.1:", type=("build", "run"))
	depends_on("r-stringr@1.2:", type=("build", "run"))
	depends_on("r-sva@3.22:", type=("build", "run"))
	depends_on("r-shiny@1:", type=("build", "run"))
	depends_on("r-shinyjs@2:", type=("build", "run"))
	depends_on("r-shinybs@0.61:", type=("build", "run"))
	depends_on("r-shinywidgets@0.5.3:", type=("build", "run"))
	depends_on("r-shinypanel@0.1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-xml@3.98.1.17:", type=("build", "run"))
	depends_on("r-readxl@1.3.1:", type=("build", "run"))
	depends_on("openssl@1.1:", type=("build", "link", "run"))
