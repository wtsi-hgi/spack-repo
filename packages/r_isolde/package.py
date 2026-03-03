# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsolde(RPackage):
	"""Integrative Statistics of alleLe Dependent Expression

	This package provides ISoLDE a new method for identifying imprinted genes. This method is dedicated to data arising from RNA sequencing technologies. The ISoLDE package implements original statistical methodology described in the publication below.
	"""
	
	homepage = "www.r-project.org"
	bioc = "ISoLDE" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ISoLDE_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ISoLDE/ISoLDE_1.30.0.tar.gz"]

	version("1.30.0", md5="448414b250ff7c903395638de3688411")

	depends_on("r@3.3:", type=("build", "run"))
