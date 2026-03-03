# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmerseq(RPackage):
	"""lmerSeq: An R package for fitting linear mixed models to RNA-Seq data"""
	
	homepage = "https://github.com/stop-pre16/lmerSeq"
	git = "https://github.com/stop-pre16/lmerSeq.git" 

	version("2022-07-22", commit="7e3e7595d02f223ca7bcbbcfab36e65879952ec8")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-lavasearch2", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
