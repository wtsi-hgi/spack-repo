# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnphooddata(RPackage):
	"""Additional and more complex example data for the SNPhood package

	This companion package for SNPhood provides some example datasets of a larger size than allowed for the SNPhood package. They include full and real-world examples for performing analyses with the SNPhood package.
	"""
	
	bioc = "SNPhoodData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/SNPhoodData_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/SNPhoodData/SNPhoodData_1.32.0.tar.gz"]

	version("1.32.0", sha256="0f80c56c17be2a73bb1b27a797d623198e75dec40a27bea349e43b5a6930035d")

	depends_on("r@3.2:", type=("build", "run"))

