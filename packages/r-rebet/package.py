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

	version("1.26.0", tag="RELEASE_3_21")
	version("1.20.0", sha256="bbdfd247fad8eb4ded97bbcc63b3c98734f81202ba545f399d265d9a532c0b0d")

	depends_on("r-asset", type=("build", "run"))
