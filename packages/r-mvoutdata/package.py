# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvoutdata(RPackage):
	"""affy and illumina raw data for assessing outlier detector performance

	affy and illumina raw data for assessing outlier detector performance
	"""
	
	bioc = "mvoutData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/mvoutData_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/mvoutData/mvoutData_1.38.0.tar.gz"]

	version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="7c44c64f508a2ac72864910c2af77f828efcdca84b3d38f37cbfa1cd53582b9f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-affy@1.23.4:", type=("build", "run"))
	depends_on("r-lumi", type=("build", "run"))

