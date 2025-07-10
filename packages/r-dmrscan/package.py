# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDmrscan(RPackage):
	"""Detection of Differentially Methylated Regions

	This package detects significant differentially methylated regions (for both qualitative and quantitative traits), using a scan statistic with underlying Poisson heuristics. The scan statistic will depend on a sequence of window sizes (# of CpGs within each window) and on a threshold for each window size. This threshold can be calculated by three different means: i) analytically using Siegmund et.al (2012) solution (preferred), ii) an important sampling as suggested by Zhang (2008), and a iii) full MCMC modeling of the data, choosing between a number of different options for modeling the dependency between each CpG.
	"""
	
	homepage = "https://github.com/christpa/DMRScan"
	bioc = "DMRScan" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DMRScan_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/DMRScan/DMRScan_1.24.0.tar.gz"]

	version("1.24.0", sha256="6d5560d4f9a1ae49c16cbf5a0be33d9dc04ff710d726aa342015f6fbfa028313")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpproll", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
