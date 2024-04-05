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

	version("1.30.0", md5="0670dfaee6f8d532cf3506428a5932c1")

	depends_on("r@3.1:", type=("build", "run"))

