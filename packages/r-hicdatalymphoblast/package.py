# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHicdatalymphoblast(RPackage):
	"""Human lymphoblastoid HiC data from Lieberman-Aiden et al. 2009

	The HiC data from human lymphoblastoid cell line (HindIII restriction) was retrieved from the sequence read archive and two ends of the paired reads were aligned separately with bowtie.
	"""
	
	bioc = "HiCDataLymphoblast" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/HiCDataLymphoblast_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/HiCDataLymphoblast/HiCDataLymphoblast_1.38.0.tar.gz"]

	version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="6fb7ba2db4547fc50cf1d100fb5e393149ecd54dd79a33dfd0f862ac4b71d3a8")


