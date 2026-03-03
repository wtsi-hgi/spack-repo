# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWorcs(RPackage):
	"""Workflow for Open Reproducible Code in Science

	Create reproducible and transparent research projects in 'R'.
    This package is based on the Workflow for Open
    Reproducible Code in Science (WORCS), a step-by-step procedure based on best
    practices for
    Open Science. It includes an 'RStudio' project template, several
    convenience functions, and all dependencies required to make your project
    reproducible and transparent. WORCS is explained in the tutorial paper
    by Van Lissa, Brandmaier, Brinkman, Lamprecht, Struiksma, & Vreede (2021).
    <doi:10.3233/DS-210031>.
	"""
	
	homepage = "https://github.com/cjvanlissa/worcs"
	cran = "worcs" 

	version("0.1.14", md5="8b4fb8da65f89900d602dfc150107f1c")

	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-renv", type=("build", "run"))
	depends_on("r-prereg@0.6:", type=("build", "run"))
	depends_on("r-gert", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-rticles@0.25:", type=("build", "run"))
	depends_on("r-tinytex", type=("build", "run"))
	depends_on("r-credentials", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-gh", type=("build", "run"))
	depends_on("r-xfun", type=("build", "run"))
	depends_on("pandoc@1.14:", type=("build", "link", "run"))
