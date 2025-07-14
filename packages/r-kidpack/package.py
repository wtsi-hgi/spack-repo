# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKidpack(RPackage):
	"""DKFZ kidney package

	kidney microarray data
	"""
	
	homepage = "http://www.dkfz.de/mga"
	bioc = "kidpack" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/kidpack_1.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/kidpack/kidpack_1.44.0.tar.gz"]

    version("1.50.0", tag="RELEASE_3_21")
	version("1.44.0", sha256="335500d961efce7f9f4b23bd4e901264b305d392f35a6541baf82a7933548795")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))

