# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSomaticadata(RPackage):
	"""An example cancer whole genome sequencing data for the SomatiCA package

	An example cancer whole genome sequencing data for the SomatiCA package
	"""
	
	bioc = "SomatiCAData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/SomatiCAData_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/SomatiCAData/SomatiCAData_1.40.0.tar.gz"]

	version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="62a1b6391a840a413d367440fbd18c6b6edb2dbe7bed418d41072625c26a2255")

	depends_on("r@2.14:", type=("build", "run"))

