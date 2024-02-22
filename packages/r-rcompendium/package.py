# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcompendium(RPackage):
	"""Create a Package or Research Compendium Structure

	Makes easier the creation of R package or research compendium 
    (i.e. a predefined files/folders structure) so that users can focus on the 
    code/analysis instead of wasting time organizing files. A full 
    ready-to-work structure is set up with some additional features: version 
    control, remote repository creation, CI/CD configuration (check package 
    integrity under several OS, test code with 'testthat', and build and deploy 
    website using 'pkgdown'). This package heavily relies on the R packages 
    'devtools' and 'usethis' and follows recommendations made by Wickham H. 
    (2015) <ISBN:9781491910597> and Marwick B. et al. (2018) 
    <doi:10.7287/peerj.preprints.3192v2>.
	"""
	
	homepage = "https://github.com/FRBCesab/rcompendium"
	cran = "rcompendium" 

	version("1.3", md5="4ee1e2c840ead273bad2a7512de622b7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cffr", type=("build", "run"))
	depends_on("r-clisymbols", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-gert", type=("build", "run"))
	depends_on("r-gh", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-renv", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-xfun", type=("build", "run"))
