# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnaseqpower(RPackage):
	"""Sample size for RNAseq studies

	RNA-seq, sample size
	"""
	
	bioc = "RNASeqPower" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RNASeqPower_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RNASeqPower/RNASeqPower_1.42.0.tar.gz"]

    version("1.48.0", tag="RELEASE_3_21")
	version("1.42.0", sha256="24a9f4de36a5885161ea16b3316d7e7eacbbfdd395f4b3037fcf89f1eeeb1126")

