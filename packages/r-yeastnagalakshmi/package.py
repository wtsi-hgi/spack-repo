# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYeastnagalakshmi(RPackage):
	"""Yeast genome RNA sequencing data based on Nagalakshmi et. al.

	The yeast genome data was retrieved from the sequence read archive, aligned with bwa, and converted to BAM format with samtools.
	"""
	
	bioc = "yeastNagalakshmi" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/yeastNagalakshmi_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/yeastNagalakshmi/yeastNagalakshmi_1.38.0.tar.gz"]

	version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="e00fd43bab3e556b9b43001741726c518a983fad61a88ac58eefc7f76e3f3eb4")


