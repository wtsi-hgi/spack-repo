# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFletcher2013b(RPackage):
	"""Master regulators of FGFR2 signalling and breast cancer risk

	This package reproduces the systems biology analysis for the data in package Fletcher2013a using RTN.
	"""
	
	homepage = "http://dx.doi.org/10.1038/ncomms3464"
	bioc = "Fletcher2013b" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Fletcher2013b_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/Fletcher2013b/Fletcher2013b_1.38.0.tar.gz"]

	version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="f65a489acc386628258ac16f1b42260c0c636a98fe0894df619cce159de2e7fe")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-fletcher2013a", type=("build", "run"))
	depends_on("r-rtn@1.1.2:", type=("build", "run"))
	depends_on("r-reder@1.8.1:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))

