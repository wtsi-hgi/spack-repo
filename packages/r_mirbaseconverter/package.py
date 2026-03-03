# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirbaseconverter(RPackage):
	"""A comprehensive and high-efficiency tool for converting and retrieving the information of miRNAs in different miRBase versions

	A comprehensive tool for converting and retrieving the miRNA Name, Accession, Sequence, Version, History and Family information in different miRBase versions. It can process a huge number of miRNAs in a short time without other depends.
	"""
	
	homepage = "https://github.com/taoshengxu/miRBaseConverter"
	bioc = "miRBaseConverter" 

	version("1.26.0", commit="e937593b9b1ae94ce13df50614a764c2970bbba1")

	depends_on("r@3.4:", type=("build", "run"))
