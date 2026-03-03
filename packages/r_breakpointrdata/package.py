# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBreakpointrdata(RPackage):
	"""Strand-seq data for demonstration purposes

	Strand-seq data to demonstrate functionalities of breakpointR package.
	"""
	
	homepage = "https://github.com/daewoooo/breakpointRdata"
	bioc = "breakpointRdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/breakpointRdata_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/breakpointRdata/breakpointRdata_1.20.0.tar.gz"]

	version("1.20.0", md5="e3f74132513d150cb5d5cc62bfd49586")

	depends_on("r@3.5:", type=("build", "run"))

