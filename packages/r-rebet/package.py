# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRebet(RPackage):
	"""The subREgion-based BurdEn Test (REBET)

	There is an increasing focus to investigate the association between rare variants and diseases. The REBET package implements the subREgion-based BurdEn Test which is a powerful burden test that simultaneously identifies susceptibility loci and sub-regions.
	"""
	
	bioc = "REBET" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/REBET_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/REBET/REBET_1.20.0.tar.gz"]

	version("1.20.0", md5="fc1e4bc02e112473630da74fce831189")

	depends_on("r-asset", type=("build", "run"))
