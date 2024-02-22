# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrmaexampledata(RPackage):
	"""Frma Example Data

	Data files used by the examples in frma and frmaTools packages
	"""
	
	bioc = "frmaExampleData" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/frmaExampleData_1.38.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/frmaExampleData/frmaExampleData_1.38.0.tar.gz"]

	version("1.38.0", md5="9713801ffd08145323ca4d31a3631995")

	depends_on("r@2.10:", type=("build", "run"))

	# experiment