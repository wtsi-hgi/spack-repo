# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMpfe(RPackage):
	"""Estimation of the amplicon methylation pattern distribution from bisulphite sequencing data

	Estimate distribution of methylation patterns from a table of counts from a bisulphite sequencing experiment given a non-conversion rate and read error rate.
	"""
	
	bioc = "MPFE" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MPFE_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MPFE/MPFE_1.38.0.tar.gz"]

    version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="b168279277c6594194eac92abae6f99bf451974fbf972e94675efb3e1e3dc823")

