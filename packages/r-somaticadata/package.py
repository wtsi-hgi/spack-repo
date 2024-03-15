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

	version("1.40.0", md5="31d9100d6b5fa5f95c59eda9995f2684")

	depends_on("r@2.14:", type=("build", "run"))

	# experiment