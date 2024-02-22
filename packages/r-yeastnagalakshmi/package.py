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
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/yeastNagalakshmi_1.38.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/yeastNagalakshmi/yeastNagalakshmi_1.38.0.tar.gz"]

	version("1.38.0", md5="ea5068bf2b4053452f416c56ab32736a")


	# experiment