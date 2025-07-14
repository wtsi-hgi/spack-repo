# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrisprbwa(RPackage):
	"""BWA-based alignment of CRISPR gRNA spacer sequences

	Provides a user-friendly interface to map on-targets and off-targets of CRISPR gRNA spacer sequences using bwa. The alignment is fast, and can be performed using either commonly-used or custom CRISPR nucleases. The alignment can work with any reference or custom genomes. Currently not supported on Windows machines.
	"""
	
	homepage = "https://github.com/crisprVerse/crisprBwa"
	bioc = "crisprBwa" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/crisprBwa_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/crisprBwa/crisprBwa_1.6.0.tar.gz"]

    version("1.12.0", tag="RELEASE_3_21")
	version("1.6.0", sha256="4948366cf1e7a648e4bb2767f52d78a6ba9c503d679bae0b02ba563f867889a5")

	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-crisprbase@0.99.15:", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-rbwa", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
