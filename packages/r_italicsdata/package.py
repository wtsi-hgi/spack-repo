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

	version("2.40.0", md5="e154526c43e11840acfd4c92ff1cee8f")

	depends_on("r@2:", type=("build", "run"))

