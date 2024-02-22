# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFletcher2013a(RPackage):
	"""Gene expression data from breast cancer cells under FGFR2 signalling perturbation

	The package Fletcher2013a contains time-course gene expression data from MCF-7 cells treated under different experimental systems in order to perturb FGFR2 signalling. The data comes from Fletcher et al. (Nature Comms 4:2464, 2013) where further details about the background and the experimental design of the study can be found.
	"""
	
	homepage = "http://dx.doi.org/10.1038/ncomms3464"
	bioc = "Fletcher2013a" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Fletcher2013a_1.38.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/Fletcher2013a/Fletcher2013a_1.38.0.tar.gz"]

	version("1.38.0", md5="e4c4f9a4e8b24a7a72f9c63337a0eef9")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-venndiagram", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))

	# experiment