# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REtec16s(RPackage):
	"""Individual-specific changes in the human gut microbiota after challenge with enterotoxigenic Escherichia coli and subsequent ciprofloxacin treatment

	16S rRNA gene sequencing data to study changes in the faecal microbiota of 12 volunteers during a human challenge study with ETEC (H10407) and subsequent treatment with ciprofloxacin.
	"""
	
	bioc = "etec16s" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/etec16s_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/etec16s/etec16s_1.30.0.tar.gz"]

	version("1.30.0", sha256="83047da9de03b0cd7f25faa06802f6a562a8ce0319a8c009dcce3b7228acb0aa")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-metagenomeseq@1.12:", type=("build", "run"))

