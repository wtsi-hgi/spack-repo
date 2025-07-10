# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RItalicsdata(RPackage):
	"""ITALICSData

	Data needed to use the ITALICS package
	"""
	
	homepage = "http://bioinfo.curie.fr"
	bioc = "ITALICSData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/ITALICSData_2.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/ITALICSData/ITALICSData_2.40.0.tar.gz"]

	version("2.40.0", sha256="16eb578398619c9034196e0f9397df1ca8b42699918fa29bc842d5e93116fd3b")

	depends_on("r@2:", type=("build", "run"))

