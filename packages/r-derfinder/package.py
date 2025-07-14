# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDerfinder(RPackage):
	"""Annotation-agnostic differential expression analysis of RNA-seq data at base-pair resolution via the DER Finder approach

	This package provides functions for annotation-agnostic differential expression analysis of RNA-seq data. Two implementations of the DER Finder approach are included in this package: (1) single base-level F-statistics and (2) DER identification at the expressed regions-level. The DER Finder approach can also be used to identify differentially bounded ChIP-seq peaks.
	"""
	
	homepage = "https://github.com/lcolladotor/derfinder"
	bioc = "derfinder" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/derfinder_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/derfinder/derfinder_1.36.0.tar.gz"]

    version("1.42.0", tag="RELEASE_3_21")
	version("1.36.0", sha256="01f66cce8795ebf7d18d51048aa766b306bd2c632657a9f2903cf675e9d74366")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocgenerics@0.25.1:", type=("build", "run"))
	depends_on("r-annotationdbi@1.27.9:", type=("build", "run"))
	depends_on("r-biocparallel@1.15.15:", type=("build", "run"))
	depends_on("r-bumphunter@1.9.2:", type=("build", "run"))
	depends_on("r-derfinderhelper@1.1:", type=("build", "run"))
	depends_on("r-genomeinfodb@1.3.3:", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomicfiles", type=("build", "run"))
	depends_on("r-genomicranges@1.17.40:", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-iranges@2.3.23:", type=("build", "run"))
	depends_on("r-qvalue@1.99:", type=("build", "run"))
	depends_on("r-rsamtools@1.25:", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-s4vectors@0.23.19:", type=("build", "run"))
