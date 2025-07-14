# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTerratcgadata(RPackage):
	"""OpenAccess TCGA Data on Terra as MultiAssayExperiment

	Leverage the existing open access TCGA data on Terra with well-established Bioconductor infrastructure. Make use of the Terra data model without learning its complexities. With a few functions, you can copy / download and generate a MultiAssayExperiment from the TCGA example workspaces provided by Terra.
	"""
	
	homepage = "https://github.com/waldronlab/terraTCGAdata"
	bioc = "terraTCGAdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/terraTCGAdata_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/terraTCGAdata/terraTCGAdata_1.6.0.tar.gz"]

	version("1.12.0", tag="RELEASE_3_21")
	version("1.6.0", sha256="0ea975f5dc017c484aacfaad03a22a155989b2eff441b76acab9367654b05731")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-anvil", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-raggedexperiment", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tcgautils", type=("build", "run"))
