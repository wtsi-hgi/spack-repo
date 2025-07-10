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

	version("1.20.0", sha256="b297da45e4a070b3dc7bf4467f779eca0b36ccf9d3640db9b7772a33c8dd898f")

	depends_on("r@3.5:", type=("build", "run"))

