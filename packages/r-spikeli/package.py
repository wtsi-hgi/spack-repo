# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpikeli(RPackage):
	"""Affymetrix Spike-in Langmuir Isotherm Data Analysis Tool

	SpikeLI is a package that performs the analysis of the Affymetrix spike-in data using the Langmuir Isotherm. The aim of this package is to show the advantages of a physical-chemistry based analysis of the Affymetrix microarray data compared to the traditional methods. The spike-in (or Latin square) data for the HGU95 and HGU133 chipsets have been downloaded from the Affymetrix web site. The model used in the spikeLI package is described in details in E. Carlon and T. Heim, Physica A 362, 433 (2006).
	"""
	
	bioc = "spikeLI" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/spikeLI_2.62.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/spikeLI/spikeLI_2.62.0.tar.gz"]

    version("2.68.0", tag="RELEASE_3_21")
	version("2.62.0", sha256="7639c41797ac59aaa7d22500efcc1fae51fed6c10ed56f4f65692f11ab247530")

