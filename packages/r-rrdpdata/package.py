# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrdpdata(RPackage):
	"""Database for the Default RDP Classifier

	Database used by the default RDP Classifier
	"""
	
	bioc = "rRDPData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/rRDPData_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/rRDPData/rRDPData_1.22.0.tar.gz"]

	version("1.22.0", md5="9ca56f1bf00bfaefb27c351ccc7346ae")

	depends_on("r-rrdp", type=("build", "run"))
	depends_on("openjdk", type=("build", "link", "run"))

	# experiment