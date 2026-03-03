# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPipeframe(RPackage):
	"""Pipeline framework for bioinformatics in R

	pipeFrame is an R package for building a componentized bioinformatics pipeline. Each step in this pipeline is wrapped in the framework, so the connection among steps is created seamlessly and automatically. Users could focus more on fine-tuning arguments rather than spending a lot of time on transforming file format, passing task outputs to task inputs or installing the dependencies. Componentized step elements can be customized into other new pipelines flexibly as well. This pipeline can be split into several important functional steps, so it is much easier for users to understand the complex arguments from each step rather than parameter combination from the whole pipeline. At the same time, componentized pipeline can restart at the breakpoint and avoid rerunning the whole pipeline, which may save a lot of time for users on pipeline tuning or such issues as power off or process other interrupts.
	"""
	
	homepage = "https://github.com/wzthu/pipeFrame"
	bioc = "pipeFrame" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/pipeFrame_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/pipeFrame/pipeFrame_1.18.0.tar.gz"]

	version("1.18.0", md5="142f8d049aa03cec36050c2b0ccc87d9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
