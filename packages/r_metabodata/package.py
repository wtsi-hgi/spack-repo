# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetabodata(RPackage):
	"""Example Metabolomics Data Sets

	Data sets from a variety of biological sample matrices, 
    analysed using a number of mass spectrometry based metabolomic analytical techniques.
    The example data sets are stored remotely using GitHub releases 
    <https://github.com/aberHRML/metaboData/releases> which can be accessed from R using the package.
    The package also includes the 'abr1' FIE-MS data set from the 'FIEmspro' package <https://users.aber.ac.uk/jhd/> <doi:10.1038/nprot.2007.511>.
	"""
	
	homepage = "https://aberhrml.github.io/metaboData/"
	cran = "metaboData" 

	version("0.6.3", md5="94c18efd2a14f2d6120e916f69d5659c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-piggyback", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
