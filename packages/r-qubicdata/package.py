# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQubicdata(RPackage):
	"""Data employed in the vignette of the QUBIC package

	The data employed in the vignette of the QUBIC package. These data belong to Many Microbe Microarrays Database and STRING v10.
	"""
	
	homepage = "http://github.com/zy26/QUBICdata"
	bioc = "QUBICdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/QUBICdata_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/QUBICdata/QUBICdata_1.30.0.tar.gz"]

    version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="0a2a34966c4a2a08ae0374dd79f6b921d7d1c3c0a690bf79a52eb74c75b3eb2a")

	depends_on("r@3.1:", type=("build", "run"))

