# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRscc(RPackage):
	"""R Source Code Similarity Evaluation by Variable/Function Names

	Evaluates R source codes by variable and/or functions names. Similar source codes should deliver similarity coefficients near one. Since neither the frequency nor the order of the used names is considered, a manual inspection of the R source code is required to check for similarity. Possible use cases include detection of code clones for improving
    software quality and of plagiarism amongst students' assignments.
	"""
	
	homepage = "https://github.com/sigbertklinke/rscc"
	cran = "rscc" 

	version("0.2.1", md5="240fe2cbdccd2508b2b43c573ea5c41f")

	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-formatr", type=("build", "run"))
	depends_on("r-highlight", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
