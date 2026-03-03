# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSystempiperdata(RPackage):
	"""systemPipeRdata: Workflow templates and sample data

	systemPipeRdata is a helper package to generate with a single command NGS workflow templates that are intended to be used by its parent package systemPipeR. The latter is an environment for building end-to-end analysis pipelines with automated report generation for next generation sequence (NGS) applications such as RNA-Seq, RIBO-Seq, ChIP-Seq, VAR-Seq and many others. Detailed examples for using systemPipeRdata are given in systemPipeR's overview vignette.
	"""
	
	homepage = "https://github.com/tgirke/systemPipeRdata"
	bioc = "systemPipeRdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/systemPipeRdata_2.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/systemPipeRdata/systemPipeRdata_2.6.0.tar.gz"]

	version("2.6.0", md5="1af59929fb95c3a017b88fce32a4c833")

	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-remotes", type=("build", "run"))

