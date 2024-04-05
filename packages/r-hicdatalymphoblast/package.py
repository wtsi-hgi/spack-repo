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

	version("1.38.0", md5="4e51d696b30a37414375e6987c7ab59c")


