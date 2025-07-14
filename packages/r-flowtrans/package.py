# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowtrans(RPackage):
	"""Parameter Optimization for Flow Cytometry Data Transformation

	Profile maximum likelihood estimation of parameters for flow cytometry data transformations.
	"""
	
	bioc = "flowTrans" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/flowTrans_1.54.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/flowTrans/flowTrans_1.54.0.tar.gz"]

    version("1.60.0", tag="RELEASE_3_21")
	version("1.54.0", sha256="ffc70e970ae8174e7068d812fce924e53496ea55a448d57fe129a4eedf58db61")

	depends_on("r@2.11:", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-flowviz", type=("build", "run"))
	depends_on("r-flowclust", type=("build", "run"))
