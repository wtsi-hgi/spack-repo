# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomationdata(RPackage):
	"""Experimental data for showing functionalities of the genomation package

	The package contains Chip Seq, Methylation and Cage data, downloaded from Encode
	"""
	
	bioc = "genomationData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/genomationData_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/genomationData/genomationData_1.34.0.tar.gz"]

	version("1.34.0", md5="dc03eef7730719f7c66f72ca5e9915db")


