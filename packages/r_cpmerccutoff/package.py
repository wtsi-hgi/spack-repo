# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpmerccutoff(RPackage):
	"""Calculation of Log2 Counts per Million Cutoff from ERCC Controls

	Implementation of the empirical method to derive log2 counts per million (CPM) cutoff to filter out lowly expressed genes using ERCC spike-ins as described in Goll and Bosinger et.al (2022)<doi:10.1101/2022.06.23.497396>. This package utilizes the synthetic mRNA control pairs developed by the External RNA Controls Consortium (ERCC) (ERCC 1 / ERCC 2) that are spiked into sample pairs at known ratios at various absolute abundances.  The relationship between the observed and expected fold changes is then used to empirically determine an optimal log2 CPM cutoff for filtering out lowly expressed genes.
	"""
	
	cran = "CpmERCCutoff" 

	version("1.0.0", md5="0844ad2f84bf469f5319ad9a3294058a")

	depends_on("r@3.6:", type=("build", "run"))
